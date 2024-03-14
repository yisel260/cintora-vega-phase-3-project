from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from __init__ import CURSOR, CONN


engine = create_engine('sqlite:///my_students.db')

Base = declarative_base()

class Student:

    #__table__name = 'students'

    all={}
    def __init__(self,name, last_name, period_name, class_number, id = None):
        self.id = id
        self.name = name
        self.last_name = last_name
        self.period_name = period_name
        self.class_number= class_number

        @classmethod
        def create_table(cls):
            """ Create a new table to persist the attributes of Department instances """
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            last_name TEXT,
            period_name TEXT,
            class_number INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()
        @classmethod
        def drop_table(cls):
           """ Drop the table that persists Department instances """
           sql = """
               DROP TABLE IF EXISTS departments;
             """
        CURSOR.execute(sql)
        CONN.commit()

class Group:
    all={}
    def __init__ (self,  period, name):
        self.name = name 
        self.period = period
        

    def __repr__(self):
        return f"<Group {self.id}: {self.name}>"
    
class Class:
    all = {}
    def __init__(self,period, id = None):
        self.id = id
        self.period= period
    def __repr__(self):
        return f"<Class {self.id}: {self.period}>"
    
    

    






    

