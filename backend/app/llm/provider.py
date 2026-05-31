from __future__ import annotations

import time
from typing import Any

import httpx

from ..config import settings
from ..mock_data import DB
from .types import LLMResponse


class LLMProvider:
    def __init__(self, provider: str | None = None) -> None:
        self.provider = provider or settings.default_llm_provider

    def _config(self) -> tuple[str, str]:
        if self.provider == "kimi":
            return settings.kimi_base_url, settings.kimi_api_key
        return settings.deepseek_base_url, settings.deepseek_api_key

    async def chat(
        self,
        messages: list[dict[str, str]],
        model: str | None = None,
        tools: list[dict[str, Any]] | None = None,
        response_format: dict | None = None,
        temperature: float = 0.2,
        max_tokens: int = 1200,
    ) -> LLMResponse:
        model = model or settings.default_fast_model
        base_url, api_key = self._config()
        started = time.perf_counter()
        if not api_key:
            latency = int((time.perf_counter() - started) * 1000)
            DB.append_log("llm_logs", {"provider": self.provider, "model": model, "latency_ms": latency, "mock": True, "error": None})
            return LLMResponse(content="{}", provider=self.provider, model=model, latency_ms=latency)
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                resp = await client.post(
                    f"{base_url.rstrip('/')}/chat/completions",
                    headers={"Authorization": f"Bearer {api_key}"},
                    json={
                        "model": model,
                        "messages": messages,
                        "tools": tools,
                        "response_format": response_format,
                        "temperature": temperature,
                        "max_tokens": max_tokens,
                    },
                )
                resp.raise_for_status()
                raw = resp.json()
            latency = int((time.perf_counter() - started) * 1000)
            usage = raw.get("usage", {})
            DB.append_log("llm_logs", {"provider": self.provider, "model": model, "latency_ms": latency, "usage": usage, "error": None})
            return LLMResponse(content=raw["choices"][0]["message"].get("content", ""), raw=raw, usage=usage, latency_ms=latency, provider=self.provider, model=model)
        except Exception as exc:
            latency = int((time.perf_counter() - started) * 1000)
            DB.append_log("llm_logs", {"provider": self.provider, "model": model, "latency_ms": latency, "error": str(exc)})
            return LLMResponse(content="{}", provider=self.provider, model=model, latency_ms=latency)
