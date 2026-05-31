from __future__ import annotations

import asyncio
import json
import os
import re
from typing import Any

from ..config import settings
from ..llm.provider import LLMProvider


def _extract_json(text: str) -> dict[str, Any] | None:
    text = (text or "").strip()
    if not text or text == "{}":
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        return None
    try:
        return json.loads(match.group(0))
    except json.JSONDecodeError:
        return None


def _clean_text(value: str) -> str:
    # Keep business copy plain and console-safe by removing common emoji/symbol ranges.
    return re.sub(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", "", value)


def sanitize_json(value: Any) -> Any:
    if isinstance(value, str):
        return _clean_text(value)
    if isinstance(value, list):
        return [sanitize_json(item) for item in value]
    if isinstance(value, dict):
        return {key: sanitize_json(item) for key, item in value.items()}
    return value


async def _call_llm(system: str, user: str, model: str | None = None) -> dict[str, Any] | None:
    response = await LLMProvider().chat(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        response_format={"type": "json_object"},
        temperature=0.2,
        max_tokens=1800,
    )
    return _extract_json(response.content)


def generate_json(system: str, user: str, fallback: dict[str, Any], model: str | None = None) -> dict[str, Any]:
    if os.environ.get("PYTEST_CURRENT_TEST") or os.environ.get("TEAAGENT_DISABLE_LLM") == "1":
        return fallback
    if not settings.deepseek_api_key and not settings.kimi_api_key:
        return fallback
    try:
        try:
            data = asyncio.run(_call_llm(system, user, model=model))
        except RuntimeError:
            loop = asyncio.new_event_loop()
            try:
                data = loop.run_until_complete(_call_llm(system, user, model=model))
            finally:
                loop.close()
        if isinstance(data, dict):
            merged = sanitize_json({**fallback, **data})
            return merged
    except Exception:
        return fallback
    return fallback
