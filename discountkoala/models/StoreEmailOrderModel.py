 
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class StoreEmailOrderModel(Base):
	__tablename__ = "store_email_order"

	store_email_order_id = Column("store_email_order_id", Integer, primary_key=True)
	email_token_id = Column("email_token_id", Integer, nullable=False)
  
  unique_identifier = Column(String(500), nullable=False)
