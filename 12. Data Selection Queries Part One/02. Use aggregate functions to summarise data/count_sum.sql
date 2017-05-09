/**
 * Using COUNT and SUM will give the total orders for
 * a person as well as the total amounts that they have
 * ordered.
 */
SELECT COUNT(amount), SUM(amount) FROM my_database.orders
WHERE person_id = 1;