import os
import json
from functools import lru_cache
from zipfile import Path
from avatao_startr.main.path_helper import PathHelper


@lru_cache(maxsize=1)
def load_languages():

    with open(PathHelper().supported_languages, "r") as f:
        return json.loads(f.read())


@lru_cache(maxsize=32)
def get_language_by_name(language_name):
    for language in load_languages():
        if language.get("name").lower() == language_name.lower():
            return language
    return None


@lru_cache(maxsize=32)
def get_language_folder_by_name(language_name):
    language = get_language_by_name(language_name)
    if language:
        return language.get("folder")
    return None


@lru_cache(maxsize=32)
def get_frameworks_for_language(language_name):
    language = get_language_by_name(language_name)
    if language:
        return language.get("frameworks")
    return []


@lru_cache(maxsize=1)
def get_supported_language_names():
    return [language.get("name") for language in load_languages()]


@lru_cache(maxsize=32)
def get_framework_names_for_language(language_name):
    return [
        framework.get("name")
        for framework in get_frameworks_for_language(language_name)
    ]


@lru_cache(maxsize=32)
def get_framework_folder_by_name(language_name, framework_name):
    frameworks = get_frameworks_for_language(language_name)
    for framework in frameworks:
        if framework.get("name").lower() == framework_name.lower():
            return framework.get("folder")
    return None


@lru_cache
def get_supported_modules(language_name, framework_name):
    language_folder = get_language_folder_by_name(language_name)
    if not language_folder:
        return {}
    framework_folder = get_framework_folder_by_name(language_name, framework_name)
    if not framework_folder:
        return {}

    with open(
        os.path.join(
            PathHelper().starter_kits,
            f"{language_folder}/supported_modules.json",
        ),
        "r",
    ) as language_modules:
        supported_language_modules = json.loads(language_modules.read())

    with open(
        os.path.join(
            PathHelper().starter_kits,
            f"{language_folder}/{framework_folder}/required_modules.json",
        ),
        "r",
    ) as framework_modules:
        required_framework_modules = json.loads(framework_modules.read())

    supported_language_modules["modules"]["mandatory"].extend(
        required_framework_modules.get("modules")
    )

    return supported_language_modules
