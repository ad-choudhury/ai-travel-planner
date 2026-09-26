from app.db.base import Base
from app.db.session import engine
from app.models.trip_db import Trip

Base.metadata.create_all(bind=engine)

print("Database tables created successfully")