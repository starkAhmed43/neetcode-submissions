-- Write your query below
select s.seller_name
from seller s left join orders o
on s.seller_id = o.seller_id
group by s.seller_id
having count(*) filter (where extract (year from o.sale_date) = 2020) =0
order by s.seller_name