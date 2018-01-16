-- select top 3 in the table
SELECT e1.NAME AS Employee,
       Salary
FROM   Employee e1
WHERE  3 > (SELECT Count(DISTINCT ( e2.Salary ))
            FROM   Employee e2
            WHERE  e2.Salary > e1.Salary)

--select top 3 in per group
SELECT d.NAME  AS Department,
       e1.NAME AS Employee,
       Salary
FROM   Employee e1
       JOIN Department d
         ON e1.DepartmentId = d.Id
WHERE  3 > (SELECT Count(DISTINCT ( e2.Salary ))
            FROM   Employee e2
            WHERE  e2.Salary > e1.Salary
                   AND e1.DepartmentId = e2.DepartmentId) 