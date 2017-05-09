/** complex query using concat, sum, as, and group by*/

select concat(people.first_name, ' ', people.second_name)
as fullname,
sum(orders.amount) as total_spend
from my_database.people
join my_database.orders
on people.id = orders.person_id
group by people.id;