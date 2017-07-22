from flask_sqlalchemy import SQLAlchemy
from .tables import Base

db = SQLAlchemy(metadata=Base.metadata)
