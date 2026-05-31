from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=("../.env", ".env"), extra="ignore")

    app_name: str = "TeaAgent"
    secret_key: str = "change-me-in-production"
    database_url: str = "sqlite:///./tea_agent.db"
    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com"
    kimi_api_key: str = ""
    kimi_base_url: str = "https://api.moonshot.cn/v1"
    default_llm_provider: str = "deepseek"
    default_fast_model: str = "deepseek-chat"
    default_reasoning_model: str = "deepseek-reasoner"
    default_long_context_model: str = "kimi-k2"


settings = Settings()
