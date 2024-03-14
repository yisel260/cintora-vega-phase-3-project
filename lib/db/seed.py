from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///my_students.db")
session = Session(engine, future=True)

_#Create instances of classes here..._

session.close()
session.commit()