from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class EmailTokenModel(Base):
	__tablename__ = "email_token"

	email_token_id = Column("email_token_id", Integer, primary_key=True)
	user_id = Column("user_id", Integer)

	access_token = Column(String(500), nullable=False)
	refresh_token = Column(String(500), nullable=False)