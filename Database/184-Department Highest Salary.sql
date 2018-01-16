SELECT d.NAME AS Department,
       e.NAME AS Employee,
       Salary
FROM   Employee e
       JOIN Department d
         ON e.DepartmentId = d.Id
WHERE  ( e.DepartmentId, Salary ) IN (SELECT DepartmentId,
                                             Max(Salary)
                                      FROM   Employee
                                      GROUP  BY DepartmentId) 

