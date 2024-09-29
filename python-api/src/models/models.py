from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
import uuid
from src.database.config import get_database_engine  # Import the function to get the engine

# Initialize the base class for models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String(255), unique=True, nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    firstName = Column(String(255))
    lastName = Column(String(255))
    createdAt = Column(DateTime, default=lambda: datetime.now(timezone.utc))  # Timezone-aware datetime
    updatedAt = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

# Create tables in the database
engine = get_database_engine()  # Call the function to get the engine
Base.metadata.create_all(bind=engine)
