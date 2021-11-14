from datetime import datetime

from flask import abort
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful import inputs

from app.models.event import Event


class Events(Resource):
    _get_parser = reqparse.RequestParser()
    _post_parser = reqparse.RequestParser()

    _get_parser.add_argument(
        "start_time",
        type=inputs.date,
        help="The date with the correct format is required! The correct format is YYYY-MM-DD!",
        required=False)
    _get_parser.add_argument(
        "end_time",
        type=inputs.date,
        help="The date with the correct format is required! The correct format is YYYY-MM-DD!",
        required=False)

    _post_parser.add_argument(
        "event",
        type=str,
        help="The event name is required!",
        required=True)
    _post_parser.add_argument(
        "date",
        type=inputs.date,
        help="The event date with the correct format is required! "
             "The correct format is YYYY-MM-DD!",
        required=True)

    @classmethod
    def get(cls):
        if not Event.find_all():
            return {
                "message": "There are no events."
            }

        args = cls._get_parser.parse_args()
        start_time = args["start_time"]
        end_time = args["end_time"]

        if start_time and end_time:
            events = Event.find_all_by_interval(start_time, end_time)
            if events:
                return Event.all_to_dict(items=events)

        return Event.all_to_dict()

    @classmethod
    def post(cls):
        args = cls._post_parser.parse_args()
        event_desc = args["event"]
        event_date = args["date"]

        event = Event(event=event_desc, date=event_date)
        event.save_to_db()

        return {
            "message": "The event has been added!",
            "event": event_desc,
            "date": str(event_date.date())
        }


class EventById(Resource):
    @staticmethod
    def find_event_by_id(event_id: int) -> Event:
        if not (event := Event.find_by_id(event_id)):
            abort(404, "The event doesn't exist!")
        return event

    @classmethod
    def get(cls, event_id: int):
        event = EventById.find_event_by_id(event_id)
        return event.to_dict()

    @classmethod
    def delete(cls, event_id: int):
        event = EventById.find_event_by_id(event_id)
        event.delete_from_db()
        return {"message": "The event has been deleted!"}


class EventsToday(Resource):
    @classmethod
    def get(cls):
        today = datetime.today().date()
        if not (events := Event.find_all_by_date(today)):
            return {"data": "There are no events for today!"}
        return Event.all_to_dict(items=events)
