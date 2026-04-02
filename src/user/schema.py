from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr 
    password: str = Field(..., min_length=6, max_length=255)


class UserLogin(BaseModel):
    email: EmailStr
    password: str 

class UserProfile(BaseModel):
    bio: str = Field(None, max_length=500)
    profile_image: str = Field(None, max_length=500)