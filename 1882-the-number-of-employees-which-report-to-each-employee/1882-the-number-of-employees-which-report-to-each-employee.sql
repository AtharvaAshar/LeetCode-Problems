# Write your MySQL query statement below
select e1.employee_id , e1.name ,count(*) reports_count , round(avg(e2.age)) average_age from employees e1 join employees e2 on e1.employee_id=e2.reports_to group by employee_id order by employee_id

