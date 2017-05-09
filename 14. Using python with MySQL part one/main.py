from database.mysql import MySQLDatabase
from settings import db_config

"""
Retrieve the settings from the
`db_config` dictionary to connect to
our database so we can instantiate our
MySQLDatabase object
"""
db = MySQLDatabase(db_config.get('db_name'),
                   db_config.get('user'),
                   db_config.get('pass'),
                   db_config.get('host'))

# Get all the available tables for
# our database and print them out.
tables = db.get_available_tables()
print tables

#get all the available columns for our articles table and print them out
columns = db.get_columns_for_table('articles')
print columns

columns = db.get_columns_for_table('profiles')
print columns

columns = db.get_columns_for_table('orders')
print columns

columns = db.get_columns_for_table('people')
print columns