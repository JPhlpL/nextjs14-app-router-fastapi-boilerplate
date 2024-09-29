from fastapi import FastAPI
from src.routers import user  # Import the user router from the router directory

# Initialize FastAPI and call it 'app'
app = FastAPI()

# Include the user router
app.include_router(user.router)
