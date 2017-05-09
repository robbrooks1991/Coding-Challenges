select concat("Wally West spent a total $100.00") as full_name,
sum(amount) as total from my_database.orders 
where person_id=1;