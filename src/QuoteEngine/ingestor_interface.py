"""Ingestor Interface."""
from abc import ABC, abstractmethod
from pathlib import Path
from models.quote import QuoteModel
from typing import List

class IngestorInterface(ABC):
    """Interface for Ingestor."""

    allow_extensions: list[str] = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check extensions file can ingest.

        Args:
            path (str): File path

        Returns:
            bool: true if can ingest else false
        """
        file_extension = Path(path).suffix
        return file_extension in cls.allow_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse file.

        Args:
            path (str): File path

        Returns:
            List[QuoteModel]: List of quotes
        """
        pass
