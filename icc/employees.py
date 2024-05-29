#!/usr/bin/env python

"""employees.py: Implementation of all employee types"""


class Employee:
    """
    Employee object
    """

    def __init__(self, name) -> None:
        self.name = name

    def pay_salary(self, salary: int) -> None:
        """Pay salary"""
        print(f"Paid salary {salary} for {self.name}")

    def __repr__(self) -> str:
        return f'{type(self).__name__}("self.name")'


class Accountant(Employee):
    """
    Account object
    """

    def calc_salary_for_employee(
            self, employee: Employee) -> int:
        """Calculate salary for employee"""
        print(f"{self} calculated salary for {employee.name}")
        return 1_000_000 * len(employee.name)


class Programmer(Employee):
    """
    Programmer object
    """

    def fix_bug_in_code(self, bug: int) -> None:
        """Fix bug method"""
        print(f"{self} fixed #{bug}")


class FrontendProgrammer(Programmer):
    """
    FrontEnd Programmer object
    """

    def realize_markup(self, issue: int) -> None:
        """Realization of markup by frontend programmer"""
        print(f"{self} realized markup #{issue}")


class BackendProgrammer(Programmer):
    """
    Backend Programmer object
    """

    def realize_api(self, issue: int) -> None:
        """API realization backend programmer"""
        print(f"{self} realized api {issue}")


accountant = Accountant("Sarah")
programmer = Programmer("Yogi")
fronteder = FrontendProgrammer("Sergey")
backender = BackendProgrammer("Mike")
