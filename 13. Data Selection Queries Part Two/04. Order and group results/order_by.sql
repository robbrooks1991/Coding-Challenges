/** ordering seleced data*/

select * from my_database.orders
where created_at
between
'2017-01-01 14:48:00'
and 
'2018-01-01 15:34:00'
and
amount > 12.00
order by person_id;