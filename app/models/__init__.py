from datetime import datetime
from typing import Generic
from typing import Type
from typing import TypeVar

from app import db

T = TypeVar("T", bound="BaseModel")


class BaseModel(db.Model, Generic[T]):
    __abstract__ = True

    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow())
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow(),
                           onupdate=datetime.utcnow())

    def __init__(self) -> None:
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def to_dict(self) -> dict:
        return {
            "created_on": self.created_at,
            "updated_on": self.updated_at
        }

    @classmethod
    def all_to_dict(cls, items: list[T] = None) -> list[dict]:
        return [item.to_dict() for item in (items if items else cls.find_all())]

    @classmethod
    def find_by_id(cls: Type[T], _id: int) -> T:
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_name(cls: Type[T], name: str) -> T:
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) -> list[T]:
        return cls.query.all()
