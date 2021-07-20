from dotenv import load_dotenv
load_dotenv()
from .relation import *
from sqlalchemy import create_engine
import os

engine = create_engine(url=os.getenv("MYSQL_URI"), echo=True, pool_size=20, max_overflow=0)
