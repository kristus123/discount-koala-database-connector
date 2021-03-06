from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class EmailTokenModel(Base):
	__tablename__ = "email_token"

	email_token_id = Column("email_token_id", Integer, primary_key=True)
	user_id = Column("user_id", Integer)
	
	full_email_name = Column(String(100), nullable=False)
	
	email_provider = Column(String(40), nullable=False)

	access_token = Column(String(500), nullable=False)
	refresh_token = Column(String(500), nullable=False)
	
	expired_at

	last_scraped = Column(DateTime, default=LocDate.utcnow, nullable=False)
