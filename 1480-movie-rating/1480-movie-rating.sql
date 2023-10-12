# Write your MySQL query statement below
(select name as results from MovieRating m join users u on m.
user_id=u.user_id group by u.user_id order by count(rating) desc, name limit 1)
union all
(SELECT mo.title AS results
  FROM Movies mo
  JOIN MovieRating m1 ON mo.movie_id = m1.movie_id
  WHERE MONTH(m1.created_at) = 2 AND YEAR(m1.created_at) = 2020
  GROUP BY mo.title
  ORDER BY AVG(m1.rating) DESC,mo.title
  LIMIT 1)