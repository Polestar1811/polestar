from pydantic import BaseModel


class InventoryAlert(BaseModel):
    sku_id: str
    name: str
    stock_status: str
    risk_level: str
    recommendation: dict
