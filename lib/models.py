from datetime import datetime

from faker import Faker
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Instantiate faker class
faker = Faker()

# Creating the tables
class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key = True)
    product_name = Column(String)
    product_description = Column(String)
    product_price = Column(Integer)
    product_amount = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    product_category = relationship('Category', back_populates = 'category_product')

    def __repr__(self):
        return(f'Product(product_id = {self.product_id}, product_name = {self.product_name}, product_description = {self.product_description}, product_price = {self.product_price}, product_amount = {self.product_amount}, category_id = {self.category_id})')

class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key = True)
    category_name = Column(String)
    category_product = relationship('Product', back_populates = 'product_category')

    def __repr__(self):
        return(f'Category(category_id = {self.category_id}, category_name ={self.category_name})')
        

# creating the session
engine = create_engine('sqlite:///models.db')
Base.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)

