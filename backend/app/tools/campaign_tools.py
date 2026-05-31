from uuid import uuid4

from ..mock_data import DB
from .common import ok


def create_campaign_brief(payload: dict):
    campaign = {"campaign_id": str(uuid4()), "status": "draft", **payload}
    DB.campaigns.append(campaign)
    return ok(campaign)


def create_approval_workitem(payload: dict):
    return ok({"approval_id": str(uuid4()), "status": "pending", "payload": payload})


def create_dispatch_job(payload: dict):
    return ok({"job_id": str(uuid4()), "status": "blocked_until_approved", "payload": payload})
