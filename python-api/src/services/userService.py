from src.repositories.userRepository import UserRepository
from src.schemas.schemas import User

class UserService:
    def __init__(self):
        # No need to pass db, the repository will handle it with the session decorator
        self.user_repository = UserRepository()

    def add_new_user(self, user: User) -> User:
        try:
            db_user = self.user_repository.create_user(user)
            return db_user
        except Exception as e:
            raise Exception(f"Error in UserService.add_new_user: {e}")

    def verify_existing_user(self, email: str) -> User:
        try:
            user = self.user_repository.verify_user(email)
            if not user:
                raise Exception("User not found")
            return user
        except Exception as e:
            raise Exception(f"Error in UserService.verify_existing_user: {e}")
