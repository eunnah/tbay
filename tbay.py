from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# One to many relationship between item and bids (item can have multiple bids)
# One to many relationship between user and bids (user can have multiple bids)
# One to many relationship between user and auctioning items (user can auction multiple items)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    seller_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bids_received = relationship("Bid", backref="items")
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    auctioned_items = relationship("Item", backref="users")
    bids_made = relationship("Bid", backref="users")

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    bidder_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bidded_item = Column(Integer, ForeignKey('items.id'), nullable=False)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
