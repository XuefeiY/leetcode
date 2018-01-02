"
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the query should return 200 as the second highest salary. If there is no second highest salary, then the query should return null.

+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
"

--sort top two then bottom one

--SELECT TOP 1 Salary AS SecondHighestSalary
--FROM (
--SELECT TOP 2 Salary
--FROM Employee
--ORDER BY Salary DESC)  toptwo
--ORDER BY Salary

--TOP doesn't work in mysql


--If both OFFSET and LIMIT appear, then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.
SELECT IFNULL(
(SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1),
NULL) AS SecondHighestSalary