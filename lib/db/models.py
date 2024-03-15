from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base




engine = create_engine('sqlite:///my_books.db')

Base = declarative_base()

class Books(Base):

    __table__name = 'books'

    id = Column("id",Integer, primary_key=True)
    name = Column("name", String())
    author = Column(String())
    genre= Column(String())
    rating = Column(Integer)

    if __name__ == '__main__':
        engine = create_engine('sqlite:///my_books.db')
        Base.metadata.create_all(engine)
        
    def __repr__(self):
        return f'Id: {self.id} ' \
        + f'Name: {self.name}'\
        + f'Author: {self.author}' \
        + f'Genre: {self.genre} '\
        + f'Rating: {self.rating}

"""
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
"""
    
    

    






    

