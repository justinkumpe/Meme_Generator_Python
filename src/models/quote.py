"""Quote Model."""
class QuoteModel:
    """Quote Model Class."""

    def __init__(self, body, author):
        """Initialize Quote Model.

        Args:
            body {str}: The Quote Message
            author {str}: Quote Author
        """
        self.author = author
        self.body = body

    def __repr__(self) -> str:
        """Return Quote.

        Returns:
            str: "{self.body} - {self.author}"
        """
        return f"{self.body} - {self.author}"
