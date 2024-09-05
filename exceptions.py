class ColorNotFoundError(Exception):
    """Raised when a color is not found in the dataset."""
    pass

class InvalidRGBValueError(ValueError):
    """Raised when an invalid RGB value is provided."""
    pass