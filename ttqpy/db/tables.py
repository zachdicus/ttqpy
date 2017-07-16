from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)


def create_connection_string(database):
    return "sqlite:///{}".format(database)


def create_session(connection_string, create_tables=False):
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file. example: 'sqlite:///sqlalchemy_example.db'
    engine = create_engine(connection_string)

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    if create_tables:
        Base.metadata.create_all(engine)

    # Bind the session
    Base.metadata.bind = engine

    # Create the database session
    db_session = sessionmaker(bind=engine)
    session = db_session()

    return session
