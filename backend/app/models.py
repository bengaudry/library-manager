from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    author: Mapped[str] = mapped_column(String(80))
    exemplars: Mapped[int] = mapped_column(default=1)
    position: Mapped[str] = mapped_column(String(80))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }

    def __repr__(self) -> str:
        return f"Books(id={self.id!r}, title={self.title!r}, author={self.author!r})"

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)

    def to_dict(self):
    return {
        "id": self.id
        "username": username
        "email": email
    }