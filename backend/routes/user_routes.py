from datetime import datetime
import sys
import os
from xmlrpc.client import DateTime
import sqlalchemy

from fastapi import FastAPI ,Depends,BackgroundTasks,Request,APIRouter
from pydantic import BaseModel 
from typing import Optional,List
from sqlalchemy.orm import Session
from utils.database.connector import SessionLocal,engine,Base
from models.schema.models import *
from fastapi.responses import HTMLResponse
from models.http.request.model import *
from execeptions.traceback_exceptions import traceException

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
Base.metadata.create_all(bind=engine)

@router.post("/Create_User")
def create_record(params: User, db : Session = Depends(get_db)): 
    user = UserDetails
    user.name = UserDetails.name
    user.email = UserDetails.email
    db.add(user)
    db.commit()
    return{
        "code":"Success",
        "messege": "One user-record pushed"
    }

@router.get('/all_users')
def get_users(db: Session= Depends(get_db)):
    return db.query(User).all()