from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud
from database import get_db
from schemas import OrderCreate, OrderResponse

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    new_order = crud.create_order(db, order)
    return new_order

@router.get("/", response_model = list[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return crud.get_all_orders(db)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session= Depends(get_db)):
    db_order = crud.get_order_by_id(db, order_id)

    if not db_order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    

    return db_order