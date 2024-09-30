"""Ingestor."""
from .ingestor_interface import IngestorInterface
from .csv_ingestor import CSVIngestor
from .docx_ingestor import DocxIngestor
from .pdf_ingestor import PDFIngestor
from .text_ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """Ingestor Class."""

    allow_extensions = [".csv", ".docx", ".pdf", ".txt"]

    @classmethod
    def parse(cls, path: str):
        """Parse file by path.

        Args:
            path (str): File path

        Returns:
            list: List of quotes
        """
        if not cls.can_ingest(path):
            raise ValueError("Unsupported file extension:")

        try:

            if CSVIngestor.can_ingest(path):
                return CSVIngestor.parse(path)
            if DocxIngestor.can_ingest(path):
                return DocxIngestor.parse(path)
            if PDFIngestor.can_ingest(path):
                return PDFIngestor.parse(path)
            if TextIngestor.can_ingest(path):
                return TextIngestor.parse(path)
        except Exception as error:
            raise Exception(f"Error parsing file '{path}': {error}") from error
