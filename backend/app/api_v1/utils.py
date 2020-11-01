import os
import json


def get_supported_languages():
    return {
        'supported_languages': [ f.name for f in os.scandir(os.environ.get('TFW_STARTER_LANGUAGE_TEMPLATES_DIRECTORY')) if f.is_dir() ]
    }


def get_supported_frameworks(language):
    return {
        'language': language,
        'supported_framework': [ f.name for f in os.scandir(os.path.join(os.environ.get('TFW_STARTER_LANGUAGE_TEMPLATES_DIRECTORY'), language)) if f.is_dir() ]
    }


def get_supported_modules(language, framework):
    with open(os.path.join(os.environ.get('TFW_STARTER_LANGUAGE_TEMPLATES_DIRECTORY'), f"{language}/supported_modules.json"), 'r') as language_modules:
        supported_language_modules = json.loads(language_modules.read())

    with open(os.path.join(os.environ.get('TFW_STARTER_LANGUAGE_TEMPLATES_DIRECTORY'), f"{language}/{framework}/supported_modules.json"), 'r') as framework_modules:
        supported_framework_modules = json.loads(framework_modules.read())
    
    return {
        'language_modules': supported_language_modules,
        'framework_modules': supported_framework_modules
    }
