/**
 * Example of a select query using a RIGHT join
 */
SELECT orders.id, people.first_name
FROM my_database.orders
RIGHT JOIN my_database.people
ON orders.person_id = people.id
ORDER BY orders.person_id;