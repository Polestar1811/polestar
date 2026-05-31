ROLE_PERMISSIONS = {
    "owner": {"*"},
    "admin": {"orders:read", "reports:read", "campaigns:write", "tickets:approve", "admin:read"},
    "customer_service": {"orders:read", "tickets:write", "chat:use"},
    "operations": {"products:read", "campaigns:write", "reports:read", "chat:use"},
    "warehouse": {"inventory:read", "orders:read", "chat:use"},
    "finance": {"reports:finance", "reports:read", "tickets:approve", "chat:use"},
    "viewer": {"products:read", "reports:read"},
}


def can(role: str, permission: str) -> bool:
    perms = ROLE_PERMISSIONS.get(role, set())
    return "*" in perms or permission in perms
