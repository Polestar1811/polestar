from pydantic import BaseModel


class Product(BaseModel):
    sku_id: str
    name: str
    price: float
    stock: int
    recommendable: bool
    tags: list[str]
