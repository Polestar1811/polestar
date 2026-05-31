from .provider import LLMProvider


def deepseek_provider() -> LLMProvider:
    return LLMProvider("deepseek")
