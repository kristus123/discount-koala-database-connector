import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

def _default_uri():

	db_username = os.environ.get("DB_USERNAME")
	db_password = os.environ.get("DB_PASSWORD")
	db_host     = os.environ.get("DB_HOST")
	db_database = os.environ.get("DB_DATABASE")

	url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:3306/{db_database}"


class DiscountKoalaDatabase:
	def __init__(self, uri=_default_uri()):
		engine = create_engine(uri)

		Base.metadata.create_all(bind=engine)

		Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

		self.session = self.Session()