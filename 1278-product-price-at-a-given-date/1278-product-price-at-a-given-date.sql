# Write your MySQL query statement below
select product_id , 10 as price from products group by product_id having min(change_date)>'2019-08-16' 
union all
select p.product_id , new_price price from products p inner join  (
    select product_id , max(change_date) as date from products where change_date<="2019-08-16" group by product_id
) as a on p.product_id= a.product_id and p.change_date=a.date