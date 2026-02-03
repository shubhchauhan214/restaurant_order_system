from sqlalchemy.orm import Session
from models import Order
from schemas import OrderCreate

def create_order(db: Session, order: OrderCreate):
    new_order = Order(
        item_name=order.item_name,
        quantity=order.quantity,
        status="PENDING"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_all_orders(db: Session):
    return db.query(Order).all()

def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def update_order_status(db: Session, order_id: int, new_status: str):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        return None
    
    order.status = new_status
    db.commit()
    db.refresh(order)
    return order