from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    item_name: str
    quantity: int

class OrderCreate(OrderBase):
    pass

class OrderResponse(OrderBase):
    id: int
    status: str

    class Config:
        from_attributes = True