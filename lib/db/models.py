from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///my_students.db')

Base = declarative_base()

class Student:

    all={}
    def __init__(self,name, last_name, class_name, class_number, id = None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.class_name = class_name
        self.class_number= class_number

class Group:
    all={}
    def __init__ (self,  period, name):
        self.name = name 
        self.period = period
        

    def __repr__(self):
        return f"<Group {self.id}: {self.name}>"




    

