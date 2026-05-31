from .common import ok


def query_sales_metrics(period: str = "week", filters: dict | None = None):
    return ok({"period": period, "gmv": 128600, "orders": 842, "aov": 152.7, "refund_rate": 0.032, "gross_margin": 0.38})


def query_sku_performance(period: str = "week"):
    return ok([
        {"sku_id": "SKU-LJ-001", "name": "西湖龙井礼盒", "gmv": 38600, "orders": 129},
        {"sku_id": "SKU-HC-001", "name": "茉莉花茶袋泡茶", "gmv": 18900, "orders": 386},
    ])


def query_channel_performance(period: str = "week"):
    return ok([
        {"channel": "抖音", "gmv": 52000, "conversion_rate": 0.041},
        {"channel": "小红书", "gmv": 31000, "conversion_rate": 0.028},
        {"channel": "微信私域", "gmv": 45600, "conversion_rate": 0.087},
    ])


def analyze_uploaded_excel(file_id: str):
    return ok({"file_id": file_id, "summary": "MVP 暂未解析真实文件，已预留接口。"})
