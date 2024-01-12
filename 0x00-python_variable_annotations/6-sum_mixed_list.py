#!/usr/bin/env python3
"""sum_mixed_list Module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Syntax: sum_mixed_list(mixedList)

    args:
        mxd_lst (List[Union[int, float]]): list of floats and integers

    return (float): sum of arguments passed
    """
    return sum(mxd_lst)
