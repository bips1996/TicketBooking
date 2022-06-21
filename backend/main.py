import sys,os
from fastapi.routing import APIRouter
from fastapi import FastAPI,Depends
from fastapi.responses import JSONResponse

from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware

from routes.booking_routes import router as booking_router
from routes.movie_routes import router as movie_router
from routes.user_routes import router as user_router

from utils.security.autherization import token_validation

from config.config import API_PREFIX, DEBUG, PROJECT_NAME, VERSION,ALLOWED_HOSTS

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        )
    application.include_router(booking_router,prefix=API_PREFIX, tags=["Booking"])
    application.include_router(movie_router,prefix=API_PREFIX, tags=["Movie"])
    application.include_router(user_router,prefix=API_PREFIX, tags=["User"])

    return application
app = get_application()
