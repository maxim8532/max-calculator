class InvalidNumberFormatException(Exception):
    """
    Custom exception for invalid number formats with red highlighting for problematic dots.
    """
    def __init__(self, message):
        """
        Initialize the exception with a highlighted problematic expression.

        :param message: The error message to display.
        """
        self.message = message
        super().__init__(message)
