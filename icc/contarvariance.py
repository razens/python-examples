#!/usr/bin/env python

"""contarvariance.py: Example of using contarvariance
defined method can receive type from class and his ancestor,
but can't receive descendant
"""

from collections.abc import Callable

from employees import (
    Employee, Programmer, FrontendProgrammer,
    programmer
)


def give_task_for_programmer(
        task: Callable[[Programmer], None],
        _programmer: Programmer) -> None:
    """Give task for programmer method"""
    task(_programmer)


def task_for_programmer(_programmer: Programmer) -> None:
    """Task for programmer method"""
    _programmer.fix_bug_in_code(1)


def task_for_employee(employee: Employee) -> None:
    """Task for employee method"""
    employee.pay_salary(123)


def task_for_frontender(frontender: FrontendProgrammer) -> None:
    """Task for frontender method"""
    frontender.realize_markup(123)


give_task_for_programmer(task_for_programmer, programmer)
give_task_for_programmer(task_for_employee, programmer)

# give_task_for_programmer(task_for_frontender, programmer)  # should throw error
