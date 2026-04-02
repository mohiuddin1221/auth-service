from fastapi import HTTPException


from .security import get_password_hash, create_access_token, verify_password

from .models import User, UserProfile


def create_new_user(user, db):
    # Check if the email already exists
    existing_user = db.query(User).where(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password
    print(f"Hashing password for user: {user.email}")
    hashed_password = get_password_hash(user.password)

    # Create a new user instance
    try:
        new_user = User(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=hashed_password,
        )

        # Add the new user to the database
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        print(f"User created with id={new_user.uid}")

    except Exception as e:
        db.rollback()
        print(f"Error creating user: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    token_payload = {"sub": str(new_user.uid), "email": new_user.email}

    access_token = create_access_token(data=token_payload)

    return {
        "message": "User created successfully",
        "access_token": access_token,
        "token_type": "bearer",
    }


def login_user(user, db):
    existing_user = db.query(User).where(User.email == user.email).first()
    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(user.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token_payload = {"sub": str(existing_user.uid), "email": existing_user.email}

    access_token = create_access_token(data=token_payload)
    return {"access_token": access_token, "token_type": "bearer"}


def update_user_profile(profile, db, current_user):
    userProfile = (
        db.query(UserProfile).where(UserProfile.user_uid == current_user.uid).first()
    )
    if not userProfile:
        raise HTTPException(status_code=404, detail="User not found")

    userProfile.bio = profile.bio
    userProfile.profile_image = profile.profile_image

    try:
        db.add(userProfile)
        db.commit()
        db.refresh(userProfile)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Internal Server Error")

    return {"message": "Profile updated successfully"}


def get_user_profile(db, current_user):
    userProfile = (
        db.query(UserProfile).where(UserProfile.user_uid == current_user.uid).first()
    )
    if not userProfile:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "bio": userProfile.bio,
        "profile_image": userProfile.profile_image
    }