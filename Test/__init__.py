import sqlite3
import os

# Delete the database if exists
try:
    os.remove('test.db')
except:
    pass

# Create the new one
conn = sqlite3.connect('test.db')

conn.close()
