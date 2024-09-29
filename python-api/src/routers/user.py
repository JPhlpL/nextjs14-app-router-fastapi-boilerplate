from fastapi import APIRouter, HTTPException
from src.services.userService import UserService
from src.schemas.schemas import User as UserSchema
from src.utils.logger import setup_logger

router = APIRouter(prefix="/user", tags=["users"])
logger = setup_logger() 

@router.post("/add/", response_model=UserSchema)
async def add_user(user: UserSchema):
    logger.info(f"Received request to create user: {user.username}")
    user_service = UserService()
    try:
        db_user = user_service.add_new_user(user)
        logger.info(f"User created successfully: {db_user.username}")
        return db_user
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/verify/", response_model=UserSchema)
async def verify_user_route(email: str):
    logger.info(f"Received request to verify user with email: {email}")
    user_service = UserService()
    try:
        user = user_service.verify_existing_user(email)
        logger.info(f"User verified successfully: {user.username}")
        return user
    except Exception as e:
        logger.error(f"Error verifying user: {e}")
        raise HTTPException(status_code=404, detail=str(e))
