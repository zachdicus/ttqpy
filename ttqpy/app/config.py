import os
from ttqpy.db import create_session
import sqlite3

environment = os.getenv("TTQPY_SYSTEM", "DEVELOPMENT")

if environment == "DEVELOPMENT":
    basedir = os.path.abspath(os.path.dirname(__file__))
    database = os.path.join(basedir, 'app.db')
    db_uri = 'sqlite:///' + database

    if not os.path.exists(database):
        # Create the database
        c = sqlite3.connect(database)
        c.close()

    # Load the tables
    session = create_session(db_uri, True)
    session.commit()
    session.close()
else:
    db_uri = os.getenv("DATABASE_URL")


class Config():
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'ttqpynoreply@gmail.com'
    MAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    DEBUG = True