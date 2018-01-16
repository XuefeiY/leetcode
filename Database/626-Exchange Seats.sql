SELECT ( CASE
           WHEN id % 2 = 1
                AND id != counts THEN id + 1
           WHEN id % 2 = 0 THEN id - 1
           ELSE id
         END ) 'id',
       student
FROM   seat,
       (SELECT Count(*) AS counts
        FROM   seat) AS seat_counts
ORDER BY id 
