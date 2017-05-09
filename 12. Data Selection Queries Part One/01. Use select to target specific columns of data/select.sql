/**
 * Selecting data using the WHERE condition to filter data
 */
SELECT amount, created_at AS purchased FROM my_database.orders
WHERE person_id = 1;