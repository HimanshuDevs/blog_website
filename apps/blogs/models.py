from sqlalchemy import Column, String, Integer, func, ForeignKey, DateTime, Boolean, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from apps.accounts.models import AuthUsers
from config.database import Base

class BaseModel(Base):
    __abstract__ = True
    is_active          = Column(Boolean, default=True, nullable=False)
    created_at         = Column(DateTime, nullable=False, default=func.now())
    updated_at         = Column(DateTime, nullable=True, onupdate=func.now()) 

class Blogs(BaseModel):
    __tablename__ = 'blogs_master'
    id                 = Column(Integer, primary_key=True, index=True)
    author_id          = Column(Integer, ForeignKey('auth_users.id', ondelete='RESTRICT'), nullable=False)
    title              = Column(String(100), nullable=False)
    description        = Column(Text, nullable=False)
    attachment         = Column(String(255), nullable=True)

class BlogsLikes(BaseModel):
    __tablename__ = 'blogs_likes'
    id                 = Column(Integer, primary_key=True, index=True)
    blog_id            = Column(Integer, ForeignKey('blogs_master.id', ondelete='CASCADE'), nullable=False)
    user_id            = Column(Integer, ForeignKey('auth_users.id', ondelete='CASCADE'), nullable=False)

    blog = relationship("Blogs", back_populates="likes")
    user = relationship("AuthUsers", back_populates="likes")

    __table_args__ = (
        UniqueConstraint('blog_id', 'user_id', name='uix_blog_like'),
    )

class BlogsComments(BaseModel):
    __tablename__ = 'blogs_comments'
    id                 = Column(Integer, primary_key=True, index=True)
    blog_id            = Column(Integer, ForeignKey('blogs_master.id', ondelete='RESTRICT'), nullable=False)
    sender_id          = Column(Integer, ForeignKey('auth_users.id', ondelete='RESTRICT'), nullable=False)
    comment            = Column(String(255), nullable=False)
    sub_sender_id      = Column(Integer, ForeignKey('blogs_comments.id'), nullable=True)
