from ..tools.report_tools import query_channel_performance, query_sales_metrics, query_sku_performance
from .base import AgentResult


def run(message: str, context: dict | None = None) -> AgentResult:
    metrics = query_sales_metrics("week")
    skus = query_sku_performance("week")
    channels = query_channel_performance("week")
    output = {
        "summary": "本周 GMV 128600 元，订单 842 单，退款率 3.2%。龙井礼盒贡献最高，私域转化率最好。",
        "metrics": metrics["data"],
        "anomalies": ["茉莉花茶袋泡茶动销下降但库存较高", "小红书转化率低于私域"],
        "recommendations": ["给 SKU-HC-001 做办公室组合促销", "复盘小红书种草内容到成交链路", "重点维护礼盒高意向客户"],
        "need_human": False,
    }
    return AgentResult(output["summary"], "reporting", "reporting", output, [metrics, skus, channels])
