from invalid_number_format_exception import InvalidNumberFormatException


def process_decimal_point(current_token, decimal_point_seen, next_char, expression, index):
    """
    Handles the logic for decimal points and checks for invalid usage.
    Highlights problematic dots if an error occurs.

    :param current_token: The current token being built.
    :param decimal_point_seen: Whether a decimal point has already been seen.
    :param next_char: The next character in the expression.
    :param expression: The entire expression being tokenized.
    :param index: The current index of the character in the expression.
    :return: Updated current_token and decimal_point_seen.
    :raises InvalidNumberFormatException: If the decimal point usage is invalid.
    """
    if decimal_point_seen:
        raise InvalidNumberFormatException(
            "ERROR: Two or more decimal points in one number",
            expression,
            [index]
        )
    if not next_char or not next_char.isdecimal():
        raise InvalidNumberFormatException(
            "ERROR: Decimal point is standalone",
            expression,
            [index]
        )
    current_token += "."
    return current_token, True
