import sqlite3
import os
import ttqpy.db as db

# Delete the database if exists
try:
    os.remove('test.db')
except:
    pass

# Create the new one
conn = sqlite3.connect('test.db')
conn.close()
del conn

connection_string = db.create_connection_string("test.db")
db.create_session(connection_string, True)

