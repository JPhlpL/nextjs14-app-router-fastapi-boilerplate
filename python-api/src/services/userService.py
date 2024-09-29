from src.repositories.userRepository import UserRepository
from src.schemas.schemas import User as UserSchema
from src.utils.logger import setup_logger

logger = setup_logger()

class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    def add_new_user(self, user: UserSchema) -> UserSchema:
        try:
            logger.info(f"Creating new user: {user.username}")
            db_user = self.user_repository.create_user(user)
            return db_user
        except Exception as e:
            logger.error(f"Error in UserService.add_new_user: {e}")
            raise Exception(f"Error in UserService.add_new_user: {e}")

    def verify_existing_user(self, email: str) -> UserSchema:
        try:
            logger.info(f"Verifying user with email: {email}")
            user = self.user_repository.verify_user(email)
            if not user:
                raise Exception("User not found")
            return user
        except Exception as e:
            logger.error(f"Error in UserService.verify_existing_user: {e}")
            raise Exception(f"Error in UserService.verify_existing_user: {e}")
