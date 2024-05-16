#!/usr/bin/env python

"""invariance.py: Example of using invariance
defined list can't receive any other type
"""
from .employees import (
    Employee, Programmer, FrontendProgrammer,
    accountant, backender
)

frontender_list: list[FrontendProgrammer] = []
programmers_list: list[Programmer] = []
employees_list: list[Employee] = []

programmers_list = frontender_list # should throw error, Incompatible types
programmers_list = employees_list # should throw error, Incompatible types

programmers_list = employees_list # should throw error, Incompatible types
employees_list.append(accountant)
print(f"{programmers_list=}")

programmers_list = frontender_list # should throw error, Incompatible types
programmers_list.append(backender)
print(f"{frontender_list=}")
