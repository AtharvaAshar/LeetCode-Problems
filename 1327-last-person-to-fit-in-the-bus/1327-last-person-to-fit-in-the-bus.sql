# Write your MySQL query statement below
select person_name from 
(select case when sum(weight) over (order by turn)<=1000 then turn end turn ,person_name from queue order by turn desc) a limit 1
