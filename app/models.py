from sqlalchemy import Column, Integer, Float, Boolean, DateTime
<<<<<<< HEAD
from datetime import datetime
from .db import Base
=======
from sqlalchemy.sql import func
from app.db import Base
>>>>>>> 0bf1011 (Add Streamlit dashboard and config for Render)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
<<<<<<< HEAD
    Time = Column(Float)
    V1 = Column(Float); V2 = Column(Float); V3 = Column(Float); V4 = Column(Float)
    V5 = Column(Float); V6 = Column(Float); V7 = Column(Float); V8 = Column(Float)
    V9 = Column(Float); V10 = Column(Float); V11 = Column(Float); V12 = Column(Float)
    V13 = Column(Float); V14 = Column(Float); V15 = Column(Float); V16 = Column(Float)
    V17 = Column(Float); V18 = Column(Float); V19 = Column(Float); V20 = Column(Float)
    V21 = Column(Float); V22 = Column(Float); V23 = Column(Float); V24 = Column(Float)
    V25 = Column(Float); V26 = Column(Float); V27 = Column(Float); V28 = Column(Float)
    Amount = Column(Float)
    is_fraud = Column(Boolean)
    probability = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
=======

    # Transaction features
    Time = Column(Float, nullable=False)
    V1 = Column(Float, nullable=False)
    V2 = Column(Float, nullable=False)
    V3 = Column(Float, nullable=False)
    V4 = Column(Float, nullable=False)
    V5 = Column(Float, nullable=False)
    V6 = Column(Float, nullable=False)
    V7 = Column(Float, nullable=False)
    V8 = Column(Float, nullable=False)
    V9 = Column(Float, nullable=False)
    V10 = Column(Float, nullable=False)
    V11 = Column(Float, nullable=False)
    V12 = Column(Float, nullable=False)
    V13 = Column(Float, nullable=False)
    V14 = Column(Float, nullable=False)
    V15 = Column(Float, nullable=False)
    V16 = Column(Float, nullable=False)
    V17 = Column(Float, nullable=False)
    V18 = Column(Float, nullable=False)
    V19 = Column(Float, nullable=False)
    V20 = Column(Float, nullable=False)
    V21 = Column(Float, nullable=False)
    V22 = Column(Float, nullable=False)
    V23 = Column(Float, nullable=False)
    V24 = Column(Float, nullable=False)
    V25 = Column(Float, nullable=False)
    V26 = Column(Float, nullable=False)
    V27 = Column(Float, nullable=False)
    V28 = Column(Float, nullable=False)

    Amount = Column(Float, nullable=False)

    # Prediction results
    is_fraud = Column(Boolean, nullable=False)
    probability = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
>>>>>>> 0bf1011 (Add Streamlit dashboard and config for Render)
