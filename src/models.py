from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    photo: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    video: Mapped[str] = mapped_column(String(120), nullable=False)
    caption: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "photo": self.photo,
            "video": self.video,
            "caption": self.caption,
        }



class Shop(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    photo: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    video: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "photo": self.photo,
            "video": self.video,
            "description": self.description,
        }



class DirectMessage(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    message: Mapped[str] = mapped_column(String(120), nullable=False)
    friend: Mapped[str] = mapped_column(String(60), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "message": self.message,
            "friend": self.friend,
        }
