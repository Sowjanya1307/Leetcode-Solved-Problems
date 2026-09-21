select e.name
from employee e
inner join employee m
on e.id=m.managerid
group by e.id
having count(e.id)>=5
