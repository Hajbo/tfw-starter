from starter_assembler import Assembler


class StarterConfigurator:
    """
    1. inits dependency_manager
        dep_manager inits the needed framewokr_config object
    2. configure()
            - dep_manager.install() -> this MIGHT return a docker command or None. If none, nothing happens, if list, then save it and pass to the assembler later for templating
                                    -> dependencies are sent as a dict from the endpoint dict("name":"version") + mandatory packages
            - Assembler.assemble() -> templates the Dockerfile in the language folder with the framework's docker commands
    """

    def __init__(self):
        self._language = None
        self._framework = None
        self._modules = None
        self._dependency_manager = self.__init_dependency_manager(self._language, self._framework)
        self._assembler = Assembler()

    def __init_dependency_manager(self, language, framework):
        """ Import form the starters/<language> folder and init with framework
        """
        return 1

    def configure(self):
        pass

    
    