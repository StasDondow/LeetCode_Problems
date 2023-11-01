# https://leetcode.com/problems/department-highest-salary/

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salary_by_department = employee.groupby("departmentId")["salary"].transform("max")
    result = employee[employee["salary"] == max_salary_by_department]
    result = result.merge(department, left_on="departmentId", right_on="id", how="inner")
    result = result[["name_y", "name_x", "salary"]].rename(columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"})
    result = result.drop_duplicates(subset=["Employee", "Salary"])
    return result
