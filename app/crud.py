from sqlalchemy.orm import Session
from .models import Transaction

def create_transaction(db: Session, data: dict, is_fraud: bool, probability: float):
    db_transaction = Transaction(
        Time=data["Time"],
        V1=data["V1"], V2=data["V2"], V3=data["V3"], V4=data["V4"], V5=data["V5"], V6=data["V6"],
        V7=data["V7"], V8=data["V8"], V9=data["V9"], V10=data["V10"], V11=data["V11"], V12=data["V12"],
        V13=data["V13"], V14=data["V14"], V15=data["V15"], V16=data["V16"], V17=data["V17"], V18=data["V18"],
        V19=data["V19"], V20=data["V20"], V21=data["V21"], V22=data["V22"], V23=data["V23"], V24=data["V24"],
        V25=data["V25"], V26=data["V26"], V27=data["V27"], V28=data["V28"],
        Amount=data["Amount"],
        is_fraud=is_fraud,
        probability=probability,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transactions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Transaction).offset(skip).limit(limit).all()
