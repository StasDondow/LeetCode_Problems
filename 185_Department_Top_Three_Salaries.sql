-- https://leetcode.com/problems/department-top-three-salaries/description/

WITH ranked_salaries AS (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
)

SELECT Department.name AS Department,
       ranked_salaries.name AS Employee,
       ranked_salaries.salary AS Salary
FROM ranked_salaries
JOIN Department ON ranked_salaries.departmentId = Department.id
WHERE salary_rank <= 3
