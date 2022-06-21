from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib

from config.db_config import *

#SQLALCHEMY_DATABASE_URL = "sqlite:///./Emanagement.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
host_server = HOST
db_server_port = urllib.parse.quote_plus(str(PORT))
database_name = DATABASE
db_username = urllib.parse.quote_plus(str(USER_NAME))
db_password = urllib.parse.quote_plus(str(PASSWORD))
ssl_mode = urllib.parse.quote_plus(str(SSL_MODE))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)


engine = create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()