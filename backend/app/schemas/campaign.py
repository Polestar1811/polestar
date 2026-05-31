from pydantic import BaseModel


class CampaignGenerate(BaseModel):
    goal: str = "拉新"
    sku_id: str | None = None
    channel: list[str] = []
