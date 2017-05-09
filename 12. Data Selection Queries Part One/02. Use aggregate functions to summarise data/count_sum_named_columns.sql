/**
*using the AS keyword to return more readable column names for the count and sum function
*/

select count(amount) as total_sales,
sum(amount) as total_amount_spent from my_database.orders
where person_id=1;