select name as customers
from customers as c
left join orders o
on c.id=o.customerId
where o.customerid is null;
