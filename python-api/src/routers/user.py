from fastapi import APIRouter, HTTPException
from src.services.userService import UserService
from src.schemas.schemas import User as UserSchema

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

# Route to add a new user
@router.post("/add/", response_model=UserSchema)
async def add_user(user: UserSchema):
    user_service = UserService()
    try:
        db_user = user_service.add_new_user(user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route to verify a user by email
@router.post("/verify/", response_model=UserSchema)
async def verify_user_route(email: str):
    user_service = UserService()
    try:
        user = user_service.verify_existing_user(email)
        return user
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
