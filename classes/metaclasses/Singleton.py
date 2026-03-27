class Singleton(type):
    # Enforces one instance of each class with this metaclass
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # If an instance for the class does not exist, call its __call__ function to
        # create one with the args and kwargs provided
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        # Otherwise, return the existing instance for the class specified
        return cls._instances[cls]
