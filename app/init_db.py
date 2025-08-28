# app/init_db.py
from .db import Base, engine
from . import models  # Import models so SQLAlchemy knows them
from app.db import engine, Base



print("📦 Creating tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully")

