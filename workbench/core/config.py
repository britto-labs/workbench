from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    ROOT = Path.cwd()

    POSTGRES_CONTAINER = os.getenv("POSTGRES_CONTAINER")

    REDIS_CONTAINER = os.getenv("REDIS_CONTAINER")

    QDRANT_CONTAINER = os.getenv("QDRANT_CONTAINER")

    MINIO_CONTAINER = os.getenv("MINIO_CONTAINER")

    N8N_CONTAINER = os.getenv("N8N_CONTAINER")

    ADMINER_CONTAINER = os.getenv("ADMINER_CONTAINER")