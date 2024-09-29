from sqlalchemy.orm import Session
from src.models.models import User
from src.wrappers.dbSessionWrapper import with_db_session
from sqlalchemy import select
import logging

logger = logging.getLogger(__name__)

class UserRepository:
    @with_db_session
    def create_user(self, user: User, scoped_db: Session) -> User:
        try:
            logger.info(f"Creating user: {user.username}")
            db_user = User(
                email=user.email,
                username=user.username,
                password=user.password,
                firstName=user.firstName,
                lastName=user.lastName
            )
            scoped_db.add(db_user)
            scoped_db.commit()
            scoped_db.refresh(db_user)
            logger.info(f"User created successfully: {db_user.username}")
            return db_user
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise Exception(f"Error in UserRepository.create_user: {e}")

    @with_db_session
    def verify_user(self, email: str, scoped_db: Session) -> User:
        try:
            logger.info(f"Verifying user by email: {email}")
            query = select(User).where(User.email == email)
            user = scoped_db.execute(query).scalar_one_or_none()
            return user
        except Exception as e:
            logger.error(f"Error verifying user: {e}")
            raise Exception(f"Error in UserRepository.verify_user: {e}")
