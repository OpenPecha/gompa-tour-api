from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from prisma import Prisma
from model.enum import Role
from Config.connection import get_db

router = APIRouter()


# Pydantic models for request & response validation
class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: Optional[Role] = Role.USER

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[Role] = None

class UserResponse(UserBase):
    id: str

    class Config:
        from_attributes = True

# Create a new user

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Prisma = Depends(get_db)):
    try:
        # Check if the user already exists by email
        existing_user = await db.user.find_unique(where={"email": user.email})
        
        if existing_user:
            return existing_user  # Return existing user if found
        
        # Create new user if not found
        new_user = await db.user.create(
            data={
                "username": user.username,
                "email": user.email,
                "role": user.role,
            }
        )
        return new_user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get all users
@router.get("/", response_model=List[UserResponse])
async def get_users(db: Prisma = Depends(get_db)):
    users = await db.user.find_many()
    return users

# Get a specific user by ID
@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, db: Prisma = Depends(get_db)):
    user = await db.user.find_unique(where={"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update a user
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user: UserUpdate, db: Prisma = Depends(get_db)):
    existing_user = await db.user.find_unique(where={"id": user_id})
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await db.user.update(
        where={"id": user_id},
        data=user.dict(exclude_unset=True),
    )
    return updated_user

# Delete a user
@router.delete("/{user_id}")
async def delete_user(user_id: str, db: Prisma = Depends(get_db)):
    user = await db.user.find_unique(where={"id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.user.delete(where={"id": user_id})
    return {"message": "User deleted successfully"}
