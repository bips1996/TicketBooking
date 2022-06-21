from datetime import datetime
import sqlalchemy

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

@router.post("/Create_Ticket")
def create_record(ticket_params: MovieTicket, db : Session = Depends(get_db)): 
    ticket = Tickets()
    ticket.customer = ticket_params.customer
    ticket.movie = ticket_params.movie
    ticket.ticket_price = ticket_params.ticket_price
    ticket.movie_time = ticket_params.movie_time
    ticket.created_date = ticket_params.created_date
    ticket.no_of_tickets = ticket_params.no_of_tickets
    db.add(ticket)
    db.commit()
    return{
        "code":"Success",
        "messege": "One ticket-record pushed"
    }

@router.get("/all_tickets")
def get_all_tickets(db : Session =  Depends(get_db)):
    return db.query(Tickets).all()

@router.get("/price_by_month/{first_date}/{last_date}")
async def price_by_month(first_date:datetime,last_date:datetime,db : Session =  Depends(get_db)):
    try:
        sql_query = sqlalchemy.text(f'''
        SELECT TO_CHAR(created_date, 'month') AS "month", SUM(no_of_tickets*ticket_price::numeric) AS "summary_profit"
        FROM public."tickets"
        WHERE created_date 
        BETWEEN Date('{first_date}') AND Date('{last_date}')
        GROUP BY month 
        ORDER BY month asc;
        ''')
        result = db.execute(sql_query)
        result_as_list = result. fetchall()
        return result_as_list
    except Exception as e:
        traceException(e)

@router.get("/people_visited/month/{first_date}/{last_date}")
async def price_by_month(first_date:datetime,last_date:datetime,db : Session =  Depends(get_db)):
    try:
        sql_query = sqlalchemy.text(f'''
        SELECT TO_CHAR(created_date, 'month') AS "month", SUM(no_of_tickets) AS "summary_visits"
        FROM public."tickets"
        WHERE created_date 
        BETWEEN Date('{first_date}') AND Date('{last_date}')
        GROUP BY month 
        ORDER BY month asc;
        ''')
        result = db.execute(sql_query)
        result_as_list = result. fetchall()
        return result_as_list
    except Exception as e:
        traceException(e)