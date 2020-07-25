import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]
db_host     = os.environ["DB_HOST"]
db_database = os.environ["DB_DATABASE"]

url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:3306/{db_database}"

Base = declarative_base()

class DiscountKoalaDatabase:
	def __init__(self, url=url):
		engine = create_engine(url)
		self.Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


	def create_session(self):
		return self.Session()