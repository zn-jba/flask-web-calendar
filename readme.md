# Web Calendar

## About

My solution for the [**Web Calendar**][project] project on the learning platform [**JetBrains Academy**][platform].

[platform]: https://hyperskill.org/

[project]: https://hyperskill.org/projects/170

## Functionality

An app that saves all your events to a local SQLite database. It employs a REST API powered by the Flask web framework with
the packages Flask-SQLAlchemy and Flask-RESTful.

## Setup

To create the required table start a flask shell session in root directory and run these commands:

```py
from app import db

db.create_all()
quit()
```

To run the application, open a terminal in the root directory and run this command:

```bash
flask run
```

## Endpoints

- **GET** `/event`(no args): returns a response of all events 
- **GET** `/event` (**start_time** and **end_time** args): returns a response of all events in the specified range of time
- **POST** `/event`: creates an event by the required args __event__ and __date__
- **GET** `/event/<int:event_id>`: returns a response of a specific event if it exists
- **GET** `/event/today`: returns a response about all events today

## Response format in JSON

```json
{
  "id": 1,
  "event": "description of event",
  "date": "date of event"
}
```