from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from utils.database.connector import SessionLocal,engine,Base
from models.schema.models import *
from fastapi.responses import HTMLResponse
from models.http.request.model import *
from execeptions.traceback_exceptions import traceException
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from fastapi.exceptions import HTTPException


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
    user = UserDetails()
    user.name = params.name
    user.email = params.email
    db.add(user)
    db.commit()
    return{
        "code":"Success",
        "messege": "One user-record pushed"
    }

@router.get('/all_users')
def get_users(db: Session= Depends(get_db)):
    return db.query(UserDetails).all()

# @router.post("/token")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = {'username':'Biplaba','password':'abcd@1234'}
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     hashed_password = form_data.password
#     if not hashed_password == user['password']:
#         raise HTTPException(status_code=400, detail="Incorrect username or password")

#     return {"access_token": user['username'], "token_type": "bearer"}