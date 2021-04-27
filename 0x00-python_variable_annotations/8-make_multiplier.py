#!/usr/bin/env python3
""" annotations -  functions """

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """  takes a float multiplier as argument
    and returns a function that multiplies
    a float by multiplier
    """
    def aux_fun(float: float):
        """ auxiliar function """
        return multiplier * float
    return aux_fun
