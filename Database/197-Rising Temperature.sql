SELECT w2.Id 
FROM Weather AS w1 JOIN Weather AS w2
ON DATEDIFF(w2.date, w1.date) = 1
WHERE w1.Temperature < w2.Temperature