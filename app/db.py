
from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
DB_USER = "fraud_db_jpjc_user" 
DB_PASSWORD = "TJGUo8HE9lVAVWb2cPdwZEEmnbWZBvY5" 
DB_HOST = "dpg-d2mledbuibrs73bhvm90-a.frankfurt-postgres.render.com" # external hostname 
DB_NAME = "fraud_db_jpjc" 
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}" 
engine = create_engine(DATABASE_URL, client_encoding="utf8") 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base()
