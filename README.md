# MiniCalendarLink
Building a mini CalendarLink Website

## Tech Stack:
Frontend: React <br />
Backend: Python FastAPI <br />
Database: SQLite (quick to set up, no server needed) <br />
ORM: SQLAlchemy (works great with FastAPI) <br />


## How to run backend
1. create and activate the uv virtual environment:
```
uv venv my-name
source normalvenv/Scripts/activate
```

Install dependacies
```
uv pip install -r requirements.txt
```

To run the Fastapi backend
```
fastapi dev backend/main.py
```

To run the frontend
```
cd frontend
npm start
```
