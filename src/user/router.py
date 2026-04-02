from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


from database import get_db 

from .security import get_current_user
from .models import User

from .schema import(
    UserCreate,
    UserLogin,
    UserProfile

)
from .service import (
    create_new_user,
    login_user,
    update_user_profile,
    get_user_profile
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_new_user(user, db)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)


@router.put("/profile")
def update_profile(profile: UserProfile, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return update_user_profile(profile, db, current_user)

@router.get("/profile")
def get_profile(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_user_profile(db, current_user)
