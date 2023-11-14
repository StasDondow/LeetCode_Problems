-- https://leetcode.com/problems/rising-temperature/description/

SELECT a.id
FROM Weather a
LEFT JOIN Weather b ON a.recordDate = DATE_ADD(b.recordDate, INTERVAL 1 DAY)
WHERE a.temperature > b.temperature
