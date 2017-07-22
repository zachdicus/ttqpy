import os
from ttqpy.db import create_session
import sqlite3

enviroment = os.getenv("TTQPY_SYSTEM", "DEVELOPMENT")

if enviroment == "DEVELOPMENT":
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir, 'app.db')
    db_uri = 'sqlite:///' + database

    if not os.path.exists(database):
        # Create the database
        c = sqlite3.connect(database)
        c.close()

else:
    db_uri = os.getenv("DATABASE_URL")

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Load the tables
session = create_session(SQLALCHEMY_DATABASE_URI, True)
session.commit()
session.close()