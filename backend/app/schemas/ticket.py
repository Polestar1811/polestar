from pydantic import BaseModel


class TicketCreate(BaseModel):
    ticket_type: str
    payload: dict
