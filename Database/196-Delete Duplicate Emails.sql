DELETE p1 FROM Person p1, Person p2
WHERE p1.Email=p2.Email and p1.Id > p2.Id

"
Select from two tables will get the Cartesian product of these two tables.
"