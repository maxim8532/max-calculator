class InvalidCharacterException(Exception):
    """
        Custom exception for characters that are invalid.
    """
    def __init__(self, message):
        """
        Initialize the exception with a problematic expression message.

         :param message: The error message to display.
        """
        self.message = message
        super().__init__(message)
