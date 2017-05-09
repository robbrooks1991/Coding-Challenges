/**
 * Example of a select query using LEFT joins
 */
SELECT people.first_name, orders.id
FROM my_database.people
LEFT JOIN my_database.orders
ON people.id = orders.person_id
ORDER BY people.first_name;