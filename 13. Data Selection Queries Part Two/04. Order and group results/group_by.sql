/** create a select query using GPOUP BY*/

select person_id, count(amount)
from my_database.orders group by person_id