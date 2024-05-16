#!/usr/bin/env python

"""covariance.py: Example of using covariance
sequence able receive type and his descendent,
but can't receive his ancestor
"""

from collections.abc import Sequence

from .employees import (
    Employee, Programmer,
    accountant, programmer, fronteder, backender
)

employees_seq: Sequence[Programmer] = [
    accountant, # can't receive account
    programmer,
    fronteder,
    backender,
    Employee("CT") # can't receive other type
]
