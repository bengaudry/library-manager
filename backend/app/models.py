from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(80))
    author: Mapped[str] = mapped_column(String(80))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author
        }

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, title={self.title!r}, author={self.author!r})"
