def _highlight_problems(expression, problematic_indexes):
    """
    Highlights problematic characters in the expression.

    :param expression: The original expression.
    :param problematic_indexes: List of indexes where the issues occurred.
    :return: A string with problematic characters highlighted in red.
    """
    highlighted = ""
    for i, char in enumerate(expression):
        if i in problematic_indexes:
            highlighted += f"\033[91m{char}\033[0m"  # Highlight in red
        else:
            highlighted += char
    return highlighted


class InvalidNumberFormatException(Exception):
    """Custom exception for invalid number formats with red highlighting for problematic dots."""

    def __init__(self, message, expression, problematic_indexes):
        """
        Initialize the exception with a highlighted problematic expression.

        :param message: The error message to display.
        :param expression: The original expression.
        :param problematic_indexes: A list of indexes where the problems occurred.
        """
        self.message = message
        self.expression = _highlight_problems(expression, problematic_indexes)
        super().__init__(f"{self.message}\nProblematic Expression: {self.expression}")
