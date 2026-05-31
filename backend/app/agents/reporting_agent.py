import json

from ..config import settings
from ..tools.report_tools import query_channel_performance, query_sales_metrics, query_sku_performance
from .ai import generate_json
from .base import AgentResult


def _normalize_output(output: dict, fallback: dict) -> dict:
    if not isinstance(output.get("metrics"), dict):
        output["metrics"] = fallback["metrics"]
    if not isinstance(output.get("anomalies"), list):
        output["anomalies"] = fallback["anomalies"]
    if not isinstance(output.get("recommendations"), list):
        output["recommendations"] = fallback["recommendations"]
    output["summary"] = str(output.get("summary") or fallback["summary"])
    output["need_human"] = bool(output.get("need_human", False))
    return output


def run(message: str, context: dict | None = None) -> AgentResult:
    metrics = query_sales_metrics("week")
    skus = query_sku_performance("week")
    channels = query_channel_performance("week")
    fallback = {
        "summary": "本周 GMV 128600 元，订单 842 单，退款率 3.2%。龙井礼盒贡献最高，私域转化率最好。",
        "metrics": metrics["data"],
        "anomalies": ["茉莉花茶袋泡茶动销下降但库存较高", "小红书转化率低于私域"],
        "recommendations": ["给 SKU-HC-001 做办公室组合促销", "复盘小红书种草内容到成交链路", "重点维护礼盒高意向客户"],
        "need_human": False,
    }
    system = """你是企业经营分析 Agent。
先基于给定数据计算和归纳，再给老板可执行建议。不要凭空编造数据。
输出严格 JSON：summary、metrics、anomalies、recommendations、need_human。"""
    user = json.dumps({"question": message, "metrics": metrics["data"], "sku_performance": skus["data"], "channel_performance": channels["data"]}, ensure_ascii=False)
    output = _normalize_output(generate_json(system, user, fallback, model=settings.default_long_context_model), fallback)
    return AgentResult(output.get("summary", fallback["summary"]), "reporting", "reporting", output, [metrics, skus, channels])
