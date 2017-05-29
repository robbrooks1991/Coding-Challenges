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

#get all the records from the people table
results = db.select('people')

for row in results:
    print row


#selecting columns with named tuples
results = db.select('people',
                    columns = ['id', 'first_name'], named_tuples=True)
for row in results:
    print row.id, row.first_name

# We can also do more complex queries using `CONCAT`
# and `SUM`
people = db.select( 'people', columns=["CONCAT(first_name, ' ', second_name)"
                                       " AS full_name", "SUM(amount)"
                                                        " AS total_spend"],
                    named_tuples=True, where="people.id=8",
                    join="orders ON people.id=orders.person_id" )

for person in people:
    print person.full_name, "spent ", person.total_spend


# Inserting an order
db.insert('orders', person_id="2", amount="120.00")

#select a person from people table and get the average amount they spend, create a column that reads "First name spends ..."

