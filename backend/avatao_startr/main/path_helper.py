import os
import datetime
import secrets
from functools import cached_property
from avatao_startr.utils import SingletonMeta
from avatao_startr import config


class PathHelper(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.starter_workdir = config.STARTER_WORKDIR
        self.starter_sourcedir = config.STARTER_SOURCEDIR

    @staticmethod
    def generate_workdir_name():
        return f'startr-{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}'

    @staticmethod
    def generate_uuid():
        return secrets.token_hex(8)

    @cached_property
    def tfw_template_base(self):
        return os.path.join(self.starter_sourcedir, "tfw_base")

    @cached_property
    def starter_kits(self):
        return os.path.join(self.starter_sourcedir, "starter_kits")

    @cached_property
    def supported_languages(self):
        return os.path.join(self.starter_kits, "languages.json")

    @cached_property
    def dockerfile_template_source(self):
        return os.path.join(self.starter_sourcedir, "templates", "Dockerfile.jinja")

    def get_dockerfile_destination(self, starter_uuid, starter_workdir_folder_name):
        return os.path.join(
            self.starter_workdir,
            starter_uuid,
            starter_workdir_folder_name,
            "solvable",
            "Dockerfile",
        )

    @cached_property
    def supervisor_config_source(self):
        return os.path.join(
            self.starter_sourcedir, "templates", "webservice.conf.jinja"
        )

    def get_supervisor_config_destination(
        self, starter_uuid, starter_workdir_folder_name
    ):
        return os.path.join(
            self.starter_workdir,
            starter_uuid,
            starter_workdir_folder_name,
            "solvable",
            "supervisor",
            "webservice.conf",
        )

    def get_webservice_destination(self, starter_uuid, starter_workdir_folder_name):
        return os.path.join(
            self.starter_workdir,
            starter_uuid,
            starter_workdir_folder_name,
            "solvable",
            "src",
            "webservice",
        )

    def get_templating_workdir_path(self, starter_uuid, starter_workdir_folder_name):
        return os.path.join(
            self.starter_workdir, starter_uuid, starter_workdir_folder_name
        )

    def get_workdir_path(self, starter_uuid):
        return os.path.join(self.starter_workdir, starter_uuid)
