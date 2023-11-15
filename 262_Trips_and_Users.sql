-- https://leetcode.com/problems/trips-and-users/

WITH unbanned AS (
    SELECT t.request_at,
           t.status
    FROM Trips t
    LEFT JOIN Users u1 ON t.client_id = u1.users_id
    LEFT JOIN Users u2 ON t.driver_id = u2.users_id
    WHERE u1.banned != 'Yes' AND u2.banned != 'Yes'
        AND request_at BETWEEN '2013-10-01' AND '2013-10-03'
)

SELECT request_at AS Day,
    ROUND(COUNT(CASE WHEN status != 'completed' THEN 1 END) / COUNT(*), 2) AS 'Cancellation Rate'
FROM unbanned
GROUP BY request_at
