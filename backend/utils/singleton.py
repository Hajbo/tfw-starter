class SingletonMeta(type):
    """
    Simple singleton implementation.
    The singleton objects will be created during the app creation
    so we don't have to make it thread safe.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
