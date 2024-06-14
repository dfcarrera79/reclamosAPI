import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
db_uri1 = os.getenv("DB_URI1")
db_uri2 = os.getenv("DB_URI2")

# Engine for database 1
engine1 = create_engine(
    db_uri1, connect_args={}, future=True
)
SessionLocal1 = sessionmaker(
    autocommit=False, autoflush=False, bind=engine1, future=True
)

# Engine for database 2
engine2 = create_engine(
    db_uri2, connect_args={}, future=True
)
SessionLocal2 = sessionmaker(
    autocommit=False, autoflush=False, bind=engine2, future=True
)

Base = declarative_base()

# DB Utilities for database 1
def get_db1():
    db = SessionLocal1()
    try:
        yield db
    finally:
        db.close()

# DB Utilities for database 2
def get_db2():
    db = SessionLocal2()
    try:
        yield db
    finally:
        db.close()
