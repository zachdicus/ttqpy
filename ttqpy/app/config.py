import os
from ttqpy.db import create_session
import sqlite3

basedir = os.path.abspath(os.path.dirname(__file__))

database = os.path.join(basedir, 'app.db')

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + database
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False

#if not os.path.exists(database):
    # Create the database
#    c = sqlite3.connect(database)
#    c.close()

# Load the tables
session = create_session(SQLALCHEMY_DATABASE_URI, True)
session.commit()
session.close()