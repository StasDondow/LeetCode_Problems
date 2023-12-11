-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/

SELECT Employee.name
FROM (
    SELECT *, COUNT(*) AS cnt
    FROM Employee
    GROUP BY managerId
) t
LEFT JOIN Employee ON t.managerID = Employee.id
WHERE t.cnt >= 5 AND Employee.name IS NOT NULL
