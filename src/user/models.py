import uuid
from typing import Optional
from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from database import Base


# ১. User Model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uid: Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4, index=True, unique=True)

    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), unique=True, index=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    userprofile = relationship(
        "UserProfile",
        uselist=False,
        back_populates="user",
        cascade="all, delete-orphan",
    )


#  UserProfile Model
class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    uid: Mapped[uuid.UUID] = mapped_column(
        default=uuid.uuid4, index=True, unique=True
    )

    bio: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    profile_image: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    user_uid: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.uid", ondelete="CASCADE")
    )
    user = relationship("User", back_populates="userprofile")
