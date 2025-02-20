from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
