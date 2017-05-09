/** select query using joins*/

select * from my_database.people
join my_database.profiles
on
people.id = profiles.person_id;