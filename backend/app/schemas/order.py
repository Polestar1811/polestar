from pydantic import BaseModel


class Order(BaseModel):
    order_no: str
    customer_id: str
    status: str
    items: list[str]
    amount: float
