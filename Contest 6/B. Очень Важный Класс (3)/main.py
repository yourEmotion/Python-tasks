from app import VeryImportantClass, decorator
from collections.abc import Container
from numbers import Number


class HackedClass(VeryImportantClass):
    def __init__(self):
        super().__init__()

        for attr_key in dir(self):
            attr_value = super().__getattribute__(attr_key)
            if callable(attr_value) and (not attr_key.startswith("_")):
                super().__setattr__(attr_key, decorator(attr_value))

    def __getattribute__(self, attr):
        attr_value = super().__getattribute__(attr)
        if attr.startswith("_"):
            return attr_value
        if isinstance(attr_value, Number):
            return attr_value * 2
        if isinstance(attr_value, Container):
            return type(attr_value)()
        return attr_value
