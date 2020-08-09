class IngredientUnavailableException(Exception):
    """
    This exception is raised whenever an ingredient is requested which is not at all available in the inventory
    """
    pass


class IngredientInsufficientException(Exception):
    """
    This exception is raised whenever a requested ingredient quantity is not sufficiently available
    """
    pass


class IngredientShortageException(Exception):
    """
    This exception is raised whenever a requested ingredient quantity is running low in the inventory
    """
    pass


class OutletBusyException(Exception):
    pass


class FileHandlingException(Exception):
    pass


class InvalidInputOptionException(Exception):
    pass