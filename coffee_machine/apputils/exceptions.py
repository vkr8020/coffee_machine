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
    """
    This exception is raised when all outlets are in PROCESSING state
    """
    pass


class FileHandlingException(Exception):
    """
    This exception is raised when we can't read/handle the input file
    """
    pass


class InvalidInputOptionException(Exception):
    """
    This exception is raised when the given user input option is invalid
    """
    pass