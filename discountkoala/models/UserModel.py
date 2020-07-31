from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class UserModel(Base):
	__tablename__ = "user"

	user_id = Column("user_id", Integer, primary_key=True)
