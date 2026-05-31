from .provider import LLMProvider


def kimi_provider() -> LLMProvider:
    return LLMProvider("kimi")
