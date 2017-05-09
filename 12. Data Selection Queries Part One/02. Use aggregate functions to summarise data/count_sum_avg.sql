select count(amount) as total_sales,
sum(amount) as total_amount_spent,
avg(amount) as average_spend from my_database.orders
where person_id=1;