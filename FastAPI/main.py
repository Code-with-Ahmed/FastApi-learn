from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .database import SessionLocal, engine
from . import models
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"]
)

# Pydantic model for the request
class TransactionBase(BaseModel):
    amount: float
    category: str
    description: str
    is_income: bool
    date: str

# Pydantic model for the response
class TransactionModel(TransactionBase):
    id: int

    class Config:
        orm_mode = True


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.post("/transactions/", response_model=TransactionModel)
async def create_transaction(
    transaction: TransactionBase, 
    db: Session = Depends(get_db)
):
    # Create a new Transaction object and add it to the database
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@app.get("/transactions/", response_model=List[TransactionModel])
async def read_transactions(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions

