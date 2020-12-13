import os
import pathlib
from typing import List
from avatao_startr.main.language_config_base import LanguageConfigBase
from avatao_startr.utils import render_template


class LanguageConfig(LanguageConfigBase):
    @property
    def docker_commands(self) -> List[str]:
        return ["RUN cd ${TFW_WEBSERVICE_DIR} && npm install"]

    @property
    def dockerfile_template_location(self) -> str:
        return os.path.join(
            pathlib.Path(__file__).parent.absolute(), "Dockerfile.jinja"
        )

    def install_modules(self, module_list):
        render_template(
            template_file=os.path.join(
                self._webservice_folder_path, "package.json.jinja"
            ),
            destination_file=os.path.join(self._webservice_folder_path, "package.json"),
            data=module_list,
        )
        os.remove(os.path.join(self._webservice_folder_path, "package.json.jinja"))
