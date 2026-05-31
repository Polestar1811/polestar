from pydantic import BaseModel


class ReportSummary(BaseModel):
    summary: str
    metrics: dict
    anomalies: list[str]
    recommendations: list[str]
