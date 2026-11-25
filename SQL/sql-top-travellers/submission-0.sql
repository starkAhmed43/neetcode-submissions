-- Write your query below
select
    u.name,
    case
        when sum(distance) > 0
        then sum(distance)
        else 0
    end as travelled_distance
from users u left join rides r
on u.id = r.user_id
group by u.id
order by travelled_distance desc, u.name