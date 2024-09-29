"""DOCX Ingestor"""

from docx import Document
from models.quote import QuoteModel
from .ingestor_interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """DOCX Ingestor Class"""

    allow_extensions = [".docx"]

    @classmethod
    def parse(cls, path):
        """Parse DOCX file

        Args:
            path (str): File path

        Returns:
            list: List of quotes from docx file
        """

        document = Document(path)
        contents = []
        for paragraph in document.paragraphs:
            if paragraph.text:
                contents.append(
                    QuoteModel(*paragraph.text.replace('"', "").split(" - "))
                )
        return contents
