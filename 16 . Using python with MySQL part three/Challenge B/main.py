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

#create a new person in the people table

db.insert('people', first_name="Jane", second_name="Brooks", DOB='STR_TO_DATE("26-03-1955", "%d-%m-%Y")')

#add in a profile row

db.insert('profiles', person_id='9', address="Millhouse")

#add two orders of random value

db.insert('orders', person_id='9', amount="25")
db.insert('orders', person_id='9', amount="35")