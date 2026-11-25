-- Write your query below
select distinct on (student_id) *
from exam_results
order by student_id asc, score desc, exam_id asc