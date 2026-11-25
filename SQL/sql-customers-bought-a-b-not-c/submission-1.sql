-- Write your query below
select c.customer_id, c.customer_name
from customers c left join orders o
on o.customer_id = c.customer_id
group by c.customer_id, c.customer_name
having
    count(*) filter (where o.product_name = 'A') > 0
    and count(*) filter (where o.product_name = 'B') > 0
    and count(*) filter (where o.product_name = 'C') = 0
order by customer_name