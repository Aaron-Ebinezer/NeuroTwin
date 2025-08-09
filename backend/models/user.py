from datetime import datetime
from sqlalchemy import ForeignKey, String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50),unique = True)
    password_hash: Mapped[str] = mapped_column(String(128))
    tier: Mapped[str] = mapped_column(String(20), default="basic")
    initial_assessment: Mapped[float] = mapped_column(Float, default = 1.0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    feedbacks: Mapped[list["Feedback"]] = relationship(back_populates = "user")


class Feedback(Base):
    __tablename__ = "feedbacks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    rating: Mapped[str] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String(200),nullable = True)
    created_at: Mapped[datetime] = mapped_column(DateTime,default = datetime.utcnow)
    user: Mapped["User"] = relationship(back_populates = "feedbacks")
