-- https://leetcode.com/problems/delete-duplicate-emails/description/

DELETE FROM Person
WHERE id NOT IN (
    SELECT _id
    FROM (
        SELECT MIN(id) AS _id
        FROM Person
        GROUP BY email
    ) t
)
