INSERT INTO my_database.people (
    first_name,
    second_name,
    DOB
) values
	('Lizzie', 'Brooks', str_to_date('14/10/1986', '%d/%m/%Y')),
	('Helen', 'Mercer', str_to_date('10/03/1991', '%d/%m/%Y')),
    ('Robert', 'Brooks', str_to_date('20/02/1991', '%d/%m/%Y'));
    
    