from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from src.services.userService import UserService
from src.schemas.schemas import User as UserSchema
from src.utils.logger import setup_logger
import requests
from uuid import UUID

router = APIRouter(prefix="/user", tags=["users"])
logger = setup_logger() 

@router.post("/add/", response_model=UserSchema)
async def add_user_endpoint(user: UserSchema):
    logger.info(f"Received request to create user: {user.username}")
    user_service = UserService()
    try:
        db_user = user_service.add_new_user(user)
        logger.info(f"User created successfully: {db_user.username}")
        return db_user
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/update/{user_id}", response_model=UserSchema)
async def update_user_endpoint(user_id: UUID, user: UserSchema):
    logger.info(f"Received request to create user: {user.username}")
    user_service = UserService()
    try:
        db_user = user_service.update_user(user_id, user)
        logger.info(f"User created successfully: {db_user.username}")
        return db_user
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/get/{user_id}", response_model=UserSchema)
async def get_user(user_id: UUID, user_service: UserService = Depends()):
    try:
        return user_service.get_user(user_id)
    except HTTPException as e:
        raise e

@router.delete("/delete/{user_id}")
async def delete_user(user_id: UUID, user_service: UserService = Depends())  -> JSONResponse:
    try:
        result = user_service.delete_user(user_id)
        return JSONResponse({"status": result}) 
    except HTTPException as e:
        raise e