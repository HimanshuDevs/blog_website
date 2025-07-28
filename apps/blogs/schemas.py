from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey, func 
from config.database import Base
from apps.accounts.models import AuthUsers


class BaseModel(Base):
    __abstract__ = True
    is_active          = Column(Boolean, default=True)
    created_at         = Column(DateTime, default=func.now())
    updated_at         = Column(DateTime, onupdate=func.now())
