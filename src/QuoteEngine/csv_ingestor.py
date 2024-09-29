"""CSV Ingestor"""

import pandas
from models.quote import QuoteModel
from .ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """CSV Ingestor Class"""

    allow_extensions = [".csv"]

    @classmethod
    def parse(cls, path):
        """Parse CSV file

        Args:
            path (str): File path

        Returns:
            list: List of quotes from csv file
        """

        csv = pandas.read_csv(path, header=0)
        return [QuoteModel(**row) for i, row in csv.iterrows()]
