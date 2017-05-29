from database.mysql import MySQLDatabase
from settings import db_config

"""
Retrieve the settings from the
`db_config` dictionary to connect to
our database so we can instantiate our
MySQLDatabase object
"""
db = MySQLDatabase( db_config.get( 'db_name' ),
                    db_config.get( 'user' ),
                    db_config.get( 'pass' ),
                    db_config.get( 'host' ) )

#use select to get full name and minimum amount spent

person = db.select('people', columns=["CONCAT(first_name, ' ', second_name)"
                                        " AS full_name", "MIN(amount)"
                                        " AS min_spend"],
                    named_tuples=True, where="people.first_name='Jane'",
                    join="orders ON people.id=orders.person_id" )

print person