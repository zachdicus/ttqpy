import uuid
import datetime
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(32))
    password_hash = Column(String(128))
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    email_verified = Column(Boolean)
    token = Column(String)
    token_expiration = Column(DateTime)
    admin = Column(Boolean)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __init__(self, username, first_name, last_name, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.admin = False
        self.email_verified = False

    def generate_auth_token(self, expiration=600):
        self.token_expiration = datetime.datetime.now() + datetime.timedelta(0, expiration)
        self.token = str(uuid.uuid4())

    @staticmethod
    def verify_auth_token(token):
        return True

class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)
    weight = Column(Float)

    questions = relationship("Question", back_populates="test")

    def __init__(self, name, subject, weight):
        self.name = name
        self.subject = subject
        self.weight = weight


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey('test.id'))
    question = Column(String)
    correct_answer = Column(String)
    manually_graded = Column(Boolean)
    number = Column(Integer)

    test = relationship("Test", back_populates="questions")
    options = relationship("Option", back_populates="question")
    answers = relationship("Answer", back_populates="question")

    def __init__(self, question, answer, manually_graded, number):
        self.question = question
        self.answer = answer
        self.manually_graded = manually_graded
        self.number = number


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    answer_type_id = Column(Integer, ForeignKey('answer_type.id'))
    answer = Column(String)
    question = relationship("Question", back_populates="answers")
    answer_type = relationship("AnswerType", back_populates="answers")

    def __init__(self, answer_type, answer):
        self.answer_type = answer_type
        self.answer = answer


class AnswerType(Base):
    __tablename__ = "answer_type"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    answers = relationship("Answer", back_populates="answer_type")

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            "id": self.name,
            "name": self.name
        }

class Option(Base):
    __tablename__ = "option"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("question.id"))
    value = Column(String)
    label = Column(String)

    question = relationship("Question", back_populates="options")

    def __init__(self, value, label):
        self.value = value
        self.label = label


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
