"""
Lumache - Python library for cooks and food lovers. Documented with Google docstrings
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if Kind of ingredients is invalid

    Args:
        Exception (Exception): Python Exception
    """

    pass


def get_random_ingredients(kind=None):
    """Return a list of random ingredients as strings.

    Args:
        kind (List[str], optional): Kind of ingredients. Defaults to None.

    Raises:
        lumache.InvalidKindError: If the kind is invalid.

    Returns:
        List[str]: The list of ingredients
    """

    return ["shells", "gorgonzola", "parsley"]
