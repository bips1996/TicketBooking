from fastapi import Depends,APIRouter
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

@router.post("/Create_Movie")
def create_one_movie_record(params: Movie, db : Session = Depends(get_db)): 
    movie = MovieDetails()
    movie.title = params.title
    movie.release_date =params.release_date
    db.add(movie)
    db.commit()
    return{
        "code":"Success",
        "messege": "One movie-record pushed"
    }

@router.get('/all_movies')
def get_movies(db: Session= Depends(get_db)):
    return db.query(MovieDetails).all()