"""Text Ingestor."""
from models.quote import QuoteModel
from .ingestor_interface import IngestorInterface

class TextIngestor(IngestorInterface):
    """Text Ingestor Class."""

    allow_extensions = [".txt"]

    @classmethod
    def parse(cls, path):
        """Text Ingestor.

        Args:
            path (str): File path

        Returns:
            list: List of quotes from text file
        """
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        return [QuoteModel(*quote.strip().split(" - ")) for quote in lines]
