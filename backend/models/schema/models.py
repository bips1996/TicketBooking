from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TEXT
from utils.database.connector import Base

class Tickets(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    customer = Column(Integer,ForeignKey("user_details.id"))
    movie = Column(Integer,ForeignKey("movie_details.id"))
    created_date = Column(DateTime)
    movie_time = Column(DateTime)
    ticket_price = Column(Float)

class UserDetails(Base):
    __tablename__="user_details"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)

class MovieDetails(Base):
    __tablename__="movie_details"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    release_date = Column(DateTime)
