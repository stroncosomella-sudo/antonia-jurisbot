"""Configuración centralizada de JurisBot Chile."""

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Configuración de la aplicación con validación automática."""

    # === LLM Provider ===
    llm_provider: Literal["anthropic", "ollama"] = "anthropic"
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-sonnet-4-20250514"
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1:8b"

    # === Paths ===
    data_dir: Path = Path("./data")
    upload_dir: Path = Path("./data/uploads")
    db_path: Path = Path("./data/jurisbot.db")
    chroma_dir: Path = Path("./data/chroma")

    # === Embeddings ===
    embedding_model: str = "paraphrase-multilingual-MiniLM-L12-v2"

    # === Chunking ===
    max_chunk_size: int = 1000
    chunk_overlap: int = 200

    # === RAG ===
    retrieval_top_k: int = 8
    rerank_top_k: int = 4

    # === App ===
    app_name: str = "JurisBot Chile v3"
    debug: bool = False

    model_config = {
        "env_prefix": "JURISBOT_",
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }

    def ensure_dirs(self) -> None:
        """Crea directorios necesarios si no existen."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.chroma_dir.mkdir(parents=True, exist_ok=True)


settings = Settings()
