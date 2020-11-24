from zipfile import ZipFile
import shutil
import os
from importlib import import_module
from avatao_startr.utils import render_template
from avatao_startr.tfw.starter_kits.utils import (
    get_language_folder_by_name,
    get_framework_folder_by_name,
)
from avatao_startr.main.git_utils import init_starter_repo
from avatao_startr.main.path_helper import PathHelper


class Assembler:
    def __init__(self):
        self._language_config = None
        self._path_helper = PathHelper()
        self._uuid = self._path_helper.generate_uuid()
        self._workdir_folder_name = self._path_helper.generate_workdir_name()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.__cleanup_directory(self._path_helper.get_workdir_path(self._uuid))

    def __cleanup_directory(self, dir_path):
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)

    def __copy_base_to_working_directory(self) -> None:
        shutil.copytree(
            self._path_helper.tfw_template_base,
            self._path_helper.get_templating_workdir_path(
                self._uuid, self._workdir_folder_name
            ),
        )

    def __copy_language_template_to_working_directory(
        self, language_package, framework_package
    ):
        self.__cleanup_directory(
            self._path_helper.get_webservice_destination(
                self._uuid, self._workdir_folder_name
            )
        )
        shutil.copytree(
            os.path.join(
                self._path_helper.starter_kits,
                f"{language_package}/{framework_package}/app",
            ),
            self._path_helper.get_webservice_destination(
                self._uuid, self._workdir_folder_name
            ),
        )

    def __template_dockerfile(self):
        with open(
            self._path_helper.get_dockerfile_destination(
                self._uuid, self._workdir_folder_name
            ),
            "w+",
        ) as dockerfile:
            dockerfile.write(
                render_template(
                    path_to_template_file=self._language_config.dockerfile_template_location
                    if self._language_config.dockerfile_template_location
                    else self._path_helper.dockerfile_template_source,
                    data=self._language_config.docker_commands,
                )
            )

    def __template_supervisor_config(self):
        with open(
            self._path_helper.get_supervisor_config_destination(
                self._uuid, self._workdir_folder_name
            ),
            "w+",
        ) as dockerfile:
            dockerfile.write(
                render_template(
                    path_to_template_file=self._path_helper.supervisor_config_source,
                    data=self._language_config.supervisor_command,
                )
            )

    def __init_language_config(
        self, language_package, framework_package, webservice_folder_path
    ):
        self._language_config = import_module(
            f"avatao_startr.tfw.starter_kits.{language_package}.language_config"
        ).LanguageConfig(language_package, framework_package, webservice_folder_path)

    def __generate_zip(self) -> ZipFile:
        return shutil.make_archive(
            base_name=self._path_helper.get_templating_workdir_path(
                self._uuid, self._workdir_folder_name
            ),
            format="zip",
            root_dir=self._path_helper.get_templating_workdir_path(
                self._uuid, self._workdir_folder_name
            ),
        )

    def assemble_and_zip_starter(
        self,
        language_name,
        framework_name,
        dependency_list,
        git_user_name="startR",
        git_user_email="support@avatao.com",
    ):

        language_package = get_language_folder_by_name(language_name)
        framework_package = get_framework_folder_by_name(language_name, framework_name)

        self.__init_language_config(
            language_package,
            framework_package,
            self._path_helper.get_webservice_destination(
                self._uuid, self._workdir_folder_name
            ),
        )
        # copy base
        self.__copy_base_to_working_directory()
        # copy starter template
        self.__copy_language_template_to_working_directory(
            language_package, framework_package
        )
        # install modules
        self._language_config.install_modules(dependency_list)
        # template Dockerfile
        self.__template_dockerfile()
        # template supervisor
        self.__template_supervisor_config()
        # init git repo
        init_starter_repo(
            self._path_helper.get_templating_workdir_path(
                self._uuid, self._workdir_folder_name
            ),
            git_user_name,
            git_user_email,
        )
        # zip
        return self.__generate_zip()
