#test_employee.py
import pytest
from employee import get_employee_info

def test_get_employee_info():
    #sample data
    name = "Alice Smith"
    emp_id = "EMP202"
    department = "HR"
    salary = 60000
    #expected result
    expected_output = (
        "Employee Name: Alice Smith,"
        "ID: EMP202,"
        "Department: HR,"
        "Salary: 60000"
    )
    #Assertion
    assert get_employee_info(name, emp_id, department, salary) == expected_output