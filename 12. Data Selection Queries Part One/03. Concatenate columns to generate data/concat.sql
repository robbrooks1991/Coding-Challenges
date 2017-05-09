/** select multiple colimns using concat */

select concat(first_name, ',', second_name)
as full_name from my_database.people;