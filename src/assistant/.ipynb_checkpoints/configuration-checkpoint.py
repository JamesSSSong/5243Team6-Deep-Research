import os
from dataclasses import dataclass, fields
from typing import Any, Optional

from langchain_core.runnables import RunnableConfig
from dataclasses import dataclass

from enum import Enum


class SearchAPI(Enum):
    PERPLEXITY = "perplexity"
    TAVILY = "tavily"


@dataclass(kw_only=True)
class Configuration:
    """The configurable fields for the research assistant."""

    max_web_research_loops: int = 2
    local_llm: str = "llama3.2"
    search_api: SearchAPI = SearchAPI.TAVILY  # Default to TAVILY






    # New configuration for YouTube and Email
    youtube_api_key: Optional[str] = 'xxxx'
    email_recipient: Optional[str] = 'xxxx@gmail.com'
    smtp_server: Optional[str] = 'smtp.gmail.com'
    smtp_port: Optional[int] = 587
    smtp_username: Optional[str] = 'xxxx@gmail.com'
    smtp_password: Optional[str] = 'xxxx'

    reddit_client_id:  Optional[str] = None
    reddit_client_secret: Optional[str] = None
    reddit_user_agent: Optional[str] = "DeepResearchBot/1.0"
    reddit_max_posts:  Optional[int] = 5
    reddit_max_comments: Optional[int] = 10

    mongo_uri:     Optional[str] = None
    mongo_db:      Optional[str] = "deep_research"
    pinecone_api_key: Optional[str] = None
    pinecone_env:  Optional[str] = None
    pinecone_index: Optional[str] = None

    teams_webhook_url: Optional[str] = None




    @classmethod
    def from_runnable_config(
        cls, config: Optional[RunnableConfig] = None
    ) -> "Configuration":
        """Create a Configuration instance from a RunnableConfig."""
        configurable = (
            config["configurable"] if config and "configurable" in config else {}
        )
        values: dict[str, Any] = {
            f.name: os.environ.get(f.name.upper(), configurable.get(f.name))
            for f in fields(cls)
            if f.init
        }
        return cls(**{k: v for k, v in values.items() if v})