from flask_restful import Api


def init_api_routes(api: Api) -> None:
    from app.api.resources import Events
    api.add_resource(Events, "/event")

    from app.api.resources import EventById
    api.add_resource(EventById, "/event/<int:event_id>")

    from app.api.resources import EventsToday
    api.add_resource(EventsToday, "/event/today")
