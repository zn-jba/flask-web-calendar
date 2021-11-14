from datetime import datetime

from app.models import BaseModel
from app.models import db


class Event(BaseModel):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow())

    def __init__(self, event: str, date: datetime.date):
        self.event = event
        self.date = date
        super().__init__()

    def __str__(self) -> str:
        return f"{self.event} - {self.date}"

    def __repr__(self) -> str:
        return f"Event(id={self.id}, name={self.event}, date={self.date})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "event": self.event,
            "date": str(self.date)
        }

    @classmethod
    def find_by_event(cls, event: str) -> "Event":
        return cls.query.filter_by(event=event).first()

    @classmethod
    def find_by_date(cls, date: datetime.date) -> "Event":
        dates = cls.find_all_by_date(date)
        return dates[0] if dates else None

    @classmethod
    def find_all_by_date(cls, date: datetime.date) -> list["Event"]:
        return cls.query.filter_by(date=date).all()

    @classmethod
    def find_all_by_interval(cls,
                             start_time: datetime.date,
                             end_time: datetime.date) -> list["Event"]:
        return cls.query.filter(cls.date <= end_time,
                                cls.date >= start_time)
