from datetime import datetime
from xmlrpc.client import DateTime
from pydantic import BaseModel
from typing import Optional

# class MovieTicket(BaseModel) :
#     customer_name :str
#     title :str
#     created_date :datetime 
#     movie_time :datetime
#     ticket_price :float
#     class Config:
#         orm_mode = True

class MovieTicket(BaseModel):
    customer: int
    movie: int
    created_date: datetime
    movie_time: datetime
    ticket_price: float
    no_of_tickets:int
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str

class Movie(BaseModel):
    title:str
    release_date:datetime

