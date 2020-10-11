from zipfile import ZipFile
import shutil
import os


class Assembler:
    def __init__(self, language, framework):
        self._language = language
        self._framework = framework

    @property
    def _tfw_starter_source_directory_full_path(self) -> str:
        return os.environ.get('TFW_STARTER_SOURCE_DIRECTORY')

    @property
    def _tfw_starter_working_directory_full_path(self) -> str:
        return os.environ.get('TFW_STARTER_WORKING_DIRECTORY')

    def __copy_to_working_directory(self) -> None:
        if os.path.exists(self._tfw_starter_working_directory_full_path):
            shutil.rmtree(self._tfw_starter_working_directory_full_path)
        shutil.copytree(
            self._tfw_starter_source_directory_full_path,
            self._tfw_starter_working_directory_full_path
        )

    def __generate_and_replace_template(self) -> None:
        # Just for testing, the actual command generation
        # will be added later
        run_webservice_command = 'python3 app.py'
        language_commands = '# Testing'
        framework_commands = 'pip3 install Flask'


    def generate_zip(self) -> ZipFile:
        self.__copy_to_working_directory()
        self.__generate_and_replace_template()
        return shutil.make_archive(
            'tfw_starter',
            'zip',
            self._tfw_starter_working_directory_full_path
        )
    