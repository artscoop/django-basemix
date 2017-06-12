# coding: utf-8


def addattr(**kwargs):
    """
    Decorator to add attributes to a function

    The shortcut is most useful for admin representations
    of methods or attributes.

    Example:

    Instead of writing

    >>> def is_valid(self):
    >>>     return self.name != "foo"
    >>> is_valid.short_description = "The name for the function"
    >>> is_valid.boolean = True

    You write

    >>> @addattr(short_description="The name for the function", boolean=True)
    >>> def is_valid(self):
    >>>     return self.name != "foo"

    :param kwargs: the properties to add to a function
    """

    def decorator(func):
        for key in kwargs:
            setattr(func, key, kwargs[key])
        return func

    return decorator
