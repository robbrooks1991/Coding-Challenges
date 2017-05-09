insert into my_database.people (
	first_name,
    second_name,
    DOB

) values (
	'Chris',
    'Brooks',
    str_to_date('19/09/1953', '%d/%m/%Y')
)