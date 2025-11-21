# test_employee.py
import pytest
from employee import get_employee_info

def test_get_employee_info():
    # Sample data
    name = "Alice Smith"
    emp_id = "E202"
    department = "HR"
    salary = 60000

    # Expected result
    expected_output = (
        "Employee Name: Alice Smith, "
        "Employee ID: E202, "
        "Department: HR, "
        "Salary: 60000.00"
    )

    # Assertion
    assert get_employee_info(name, emp_id, department, salary) == expected_output
