from .common import ok


def send_internal_notification(role: str, message: str):
    return ok({"role": role, "message": message, "status": "mock_sent"})


def send_email(to: str, subject: str, body: str):
    return ok({"to": to, "subject": subject, "status": "mock_sent"})


def send_wecom_message(user_id: str, message: str):
    return ok({"user_id": user_id, "message": message, "status": "mock_sent"})
