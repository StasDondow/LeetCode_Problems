# https://leetcode.com/problems/nth-highest-salary/

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset=["salary"])
    employee = employee.sort_values(by=["salary"], ascending=False)

    if len(employee) >= N:
        return employee[["salary"]].iloc[[N - 1]].rename(columns={"salary": f"getNthHighestSalary({N})"})
    return pd.DataFrame({f"getNthHighestSalary({N})": [None]})  
