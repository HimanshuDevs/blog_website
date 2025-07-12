from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Date, func
from config.database import Base


class BaseModel(Base):
    __abstract__ = True
    is_active          = Column(Boolean, default=True, nullable=False)
    created_at         = Column(DateTime, nullable= False, default=func.now()) # func.now() uses the DB server time, not Python time
    updated_at         = Column(DateTime, nullable=True, onupdate=func.now()) # default=datetime.utcnow for python time

class RoleMaster(BaseModel):
    __tablename__ = 'role_master'
    id                 = Column(Integer, primary_key=True, index=True)
    role               = Column(String(50), nullable=False)
    role_code          = Column(String(10), nullable=True)

class AuthUsers(BaseModel):
    __tablename__ = 'auth_users'
    id                 = Column(Integer, primary_key=True, index=True)
    username           = Column(String(50), nullable=False)
    role_id            = Column(ForeignKey('role_master.id', ondelete='RESTRICT'), nullable=False) # ondelete='RESTRICT', ondelete='SET NULL', ondelete='CASCADE'
    email              = Column(String(50), nullable=True)
    profile_pic        = Column(String(255), nullable=True)
    password           = Column(String(255), nullable=True)