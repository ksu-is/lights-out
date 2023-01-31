"""
Helper functions which are not specific to any one section of the program.
Math functions, string manipulation functions, etc.
"""

def clamp(value,minimum,maximum):
    """
    Returns the given value clamped between the given minimum and maximum, i.e.,
    if the value is less than the minimum, the minimum will be returned. If the
    value is greater than the maximum, the maximum will be returned. Otherwise,
    the value will be returned.
    """
    return (max(minimum,min(value,maximum)))