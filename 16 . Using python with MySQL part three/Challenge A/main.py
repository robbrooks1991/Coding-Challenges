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



#select a person from people table and get the average amount they spend,
# create a column that reads "First name spends ..."

people = db.select( 'people', columns = ["first_name", "AVG(amount)"
                                         " AS average_spent"],
                    named_tuples=True, where="people.id=2",
                    join="orders ON people.id=orders.person_id" )

for person in people:
    print person.first_name, "spends", person.average_spent