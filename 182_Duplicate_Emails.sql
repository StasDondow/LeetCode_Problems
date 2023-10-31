-- https://leetcode.com/problems/duplicate-emails/description/

SELECT s.email AS EMail
FROM (
    SELECT email, COUNT(*) AS c
    FROM Person
    GROUP BY email
) s
WHERE c > 1
