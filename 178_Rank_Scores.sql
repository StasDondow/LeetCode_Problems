-- https://leetcode.com/problems/rank-scores/description/

SELECT Scores.score, t2.rank
FROM Scores
LEFT JOIN (
    SELECT *, ROW_NUMBER() OVER (ORDER BY score DESC) AS 'rank'
    FROM (
        SELECT DISTINCT score
        FROM Scores
        ORDER BY score
    ) t
) t2
ON Scores.score = t2.score
ORDER BY Scores.score DESC
