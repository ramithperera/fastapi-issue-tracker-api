from sqlalchemy import Column, Integer, String, Boolean, Enum as SQLEnum
from app.database import Base
from app.schemas import IssueStatus, IssuePriority

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    disabled = Column(Boolean, default=False)

class Issue(Base):
    __tablename__ = "issues"

    id = Column(String, primary_key=True, index=True) # UUID stored as string
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    priority = Column(SQLEnum(IssuePriority), default=IssuePriority.medium)
    status = Column(SQLEnum(IssueStatus), default=IssueStatus.open)