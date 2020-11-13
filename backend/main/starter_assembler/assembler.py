from zipfile import ZipFile
import shutil
import os
import datetime
from functools import cached_property
from importlib import import_module
from utils import SingletonMeta, render_template
from tfw.starters.utils import get_language_folder_by_name, get_framework_folder_by_name
from .git_utils import init_starter_repo


class Assembler(metaclass=SingletonMeta):

    def __init__(self):
        self._language_config = None
        self._file_base_name = '/tmp/tfw-starter'

    def __init_language_config(self, language, framework):
        language_folder = get_language_folder_by_name(language)
        framework_folder = get_framework_folder_by_name(language, framework)
        self._language_config = import_module(f'tfw.starters.{language_folder}.language_config').LanguageConfig(language_folder, framework_folder)
    
    @property
    def _file_name(self):
        return f'{self._file_base_name}-{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}'

    @cached_property
    def _tfw_starter_source_path(self) -> str:
        return os.environ.get('TFW_STARTER_TEMPLATE_BASE')

    @cached_property
    def _tfw_starter_workdir_path(self) -> str:
        return os.environ.get('TFW_STARTER_WORKING_DIRECTORY')

    @cached_property
    def _tfw_starter_webservice_path(self):
        return os.environ.get('TFW_STARTER_WEBSERVICE_DESTINATION')

    def __cleanup_directory(self, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

    def __copy_base_to_working_directory(self) -> None:
        self.__cleanup_directory(self._tfw_starter_workdir_path)
        shutil.copytree(
            self._tfw_starter_source_path,
            self._tfw_starter_workdir_path
        )

    def __copy_language_template_to_working_directory(self, language, framework):
        self.__cleanup_directory(self._tfw_starter_webservice_path)
        shutil.copytree(
            os.path.join(os.environ.get('TFW_STARTER_LANGUAGE_TEMPLATES_DIRECTORY'), f'{language}/{framework}/app'),
            self._tfw_starter_webservice_path
        )
        
    def __template_dockerfile(self):
        with open(os.environ.get('TFW_STARTER_DOCKERFILE_DESTINATION'), 'w+') as dockerfile:
            dockerfile.write(render_template(
                path_to_template_file = self._language_config.dockerfile_template_location,
                data = self._language_config.docker_commands
            ))

    def __template_supervisor_config(self):
        with open(os.environ.get('TFW_STARTER_SUPERVISOR_CONFIG_DESTINATION'), 'w+') as dockerfile:
            dockerfile.write(render_template(
                path_to_template_file = os.environ.get('TFW_STARTER_SUPERVISOR_CONFIG_SOURCE'),
                data = self._language_config.supervisor_command
            ))

    def __generate_zip(self) -> ZipFile:
        starter_zip = shutil.make_archive(
            self._file_name,
            'zip',
            self._tfw_starter_workdir_path
        )
        self.__cleanup_directory(self._tfw_starter_workdir_path)
        return starter_zip

    def assemble_and_zip_starter(self, language, framework, module_list, git_user_name="startR", git_user_email="support@avatao.com"):
        self.__init_language_config(language, framework)
        # copy base
        self.__copy_base_to_working_directory()
        # copy starter template
        self.__copy_language_template_to_working_directory(language, framework)
        # install modules
        self._language_config.install_modules(module_list)
        # template Dockerfile
        self.__template_dockerfile()
        # template supervisor
        self.__template_supervisor_config()
        # init git repo
        init_starter_repo(self._tfw_starter_workdir_path, git_user_name, git_user_email)
        # zip
        return self.__generate_zip()
        