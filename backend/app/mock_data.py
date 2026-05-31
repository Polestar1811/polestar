from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class MockDB:
    products: list[dict[str, Any]] = field(default_factory=list)
    orders: list[dict[str, Any]] = field(default_factory=list)
    tickets: list[dict[str, Any]] = field(default_factory=list)
    campaigns: list[dict[str, Any]] = field(default_factory=list)
    audit_logs: list[dict[str, Any]] = field(default_factory=list)
    llm_logs: list[dict[str, Any]] = field(default_factory=list)
    tool_logs: list[dict[str, Any]] = field(default_factory=list)
    users: list[dict[str, Any]] = field(default_factory=list)

    def ensure_seeded(self) -> None:
        if self.products:
            return
        self.products = [
            {"sku_id": "SKU-LJ-001", "name": "西湖龙井礼盒 250g", "price": 299, "scene": ["送礼", "商务"], "tags": ["清香", "礼盒"], "stock": 120, "recommendable": True, "margin": 0.42},
            {"sku_id": "SKU-LJ-002", "name": "龙井自饮装 125g", "price": 129, "scene": ["自饮", "入门"], "tags": ["清香", "绿茶"], "stock": 300, "recommendable": True, "margin": 0.35},
            {"sku_id": "SKU-PE-001", "name": "熟普洱茶饼 357g", "price": 168, "scene": ["自饮", "收藏"], "tags": ["醇厚", "普洱"], "stock": 80, "recommendable": True, "margin": 0.38},
            {"sku_id": "SKU-WT-001", "name": "福鼎白茶礼盒 300g", "price": 258, "scene": ["商务送礼", "节日"], "tags": ["白茶", "礼盒"], "stock": 30, "recommendable": True, "margin": 0.4},
            {"sku_id": "SKU-HC-001", "name": "茉莉花茶袋泡茶 30包", "price": 49, "scene": ["办公室", "入门"], "tags": ["花香", "袋泡"], "stock": 500, "recommendable": True, "margin": 0.3},
            {"sku_id": "SKU-OT-001", "name": "冻顶乌龙 150g", "price": 168, "scene": ["自饮", "冷泡"], "tags": ["乌龙", "回甘"], "stock": 50, "recommendable": True, "margin": 0.36},
        ]
        self.orders = [
            {"order_no": "ORD001", "customer_id": "C001", "phone_tail": "1001", "items": ["SKU-LJ-001"], "status": "已发货", "tracking": {"carrier": "顺丰", "status": "运输中", "latest": "已离开发件城市"}, "mutable": False, "amount": 299},
            {"order_no": "ORD002", "customer_id": "C002", "phone_tail": "1002", "items": ["SKU-HC-001"], "status": "待出库", "tracking": {}, "mutable": True, "amount": 49},
            {"order_no": "ORD003", "customer_id": "C003", "phone_tail": "1003", "items": ["SKU-WT-001"], "status": "已签收", "tracking": {"carrier": "京东", "status": "已签收"}, "mutable": False, "amount": 258, "issue": "礼盒破损"},
        ]
        self.users = [
            {"email": "owner@example.com", "role": "owner"},
            {"email": "cs@example.com", "role": "customer_service"},
            {"email": "ops@example.com", "role": "operations"},
            {"email": "warehouse@example.com", "role": "warehouse"},
            {"email": "finance@example.com", "role": "finance"},
        ]

    def append_log(self, kind: str, payload: dict[str, Any]) -> None:
        payload = {"created_at": datetime.utcnow().isoformat(), **payload}
        getattr(self, kind).append(payload)


DB = MockDB()
