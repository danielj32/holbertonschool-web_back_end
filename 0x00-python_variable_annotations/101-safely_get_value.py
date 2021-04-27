#!/usr/bin/env python3
""" More involved type annotations """

from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None])\
                     -> Union[Any, TypeVar('T')]:
    """ Given the parameters and the return values,
    add type annotations to the function
    """
    if key in dct:
        return dct[key]
    else:
        return default
