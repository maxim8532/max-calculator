from invalid_decimal_point_exception import InvalidDecimalPointException


def decimal_point_check(expression):
    """
    Validates the usage of decimal points in the expression.
    Marks all problematic decimal points in red.

    :param expression: The mathematical expression to validate.
    :type expression: str
    :return: The expression with problematic decimal points highlighted.
    :rtype: str
    """
    checked_expression = ""
    decimal_point_seen = False
    multiple_points = False
    stand_alone_point = False
    highlighted_point = f"\033[91m\033[1m.↙\033[0m"
    for index, char in enumerate(expression):
        next_char = expression[index + 1] if index + 1 < len(expression) else None
        prev_char = expression[index - 1] if index > 0 else None

        if char.isdecimal():
            checked_expression += char
        elif char == ".":
            # Multiple points in a single number
            if decimal_point_seen:
                checked_expression += highlighted_point
                multiple_points = True
                # Case 1: Point is the first character
            elif index == 0 and (not next_char or not next_char.isdecimal()):
                checked_expression += highlighted_point
                stand_alone_point = True
                # Case 2: Point is the last character
            elif index == len(expression) - 1 and (not prev_char or not prev_char.isdecimal()):
                checked_expression += highlighted_point
                stand_alone_point = True
                # Case 3: Point is the only character
            elif len(expression) == 1:
                checked_expression += highlighted_point
                stand_alone_point = True
                # Case 4: Point is standalone between non-decimal characters
            elif prev_char and next_char and not prev_char.isdecimal() and not next_char.isdecimal():
                checked_expression += highlighted_point
                stand_alone_point = True
        else:
            checked_expression += char
            decimal_point_seen = False  # Reset when encountering a non-decimal character

    if len(checked_expression) > len(expression):
        # Replacing special minuses for user clarity
        checked_expression = checked_expression.replace("u", "-")
        checked_expression = checked_expression.replace("s", "-")
        if multiple_points and stand_alone_point:
            raise InvalidDecimalPointException(f"{checked_expression}\n\n\033[91mInvalid Decimal Point: \033[0m"
                                               f"Stand-alone points and Multiple decimal points in one number "
                                               f"are not allowed.")
        elif multiple_points:
            raise InvalidDecimalPointException(f"{checked_expression}\n\n\033[91mInvalid Decimal Point: \033[0m"
                                               f"Multiple decimal points in one number "
                                               f"are not allowed.")
        else:
            raise InvalidDecimalPointException(f"{checked_expression}\n\n\033[91mInvalid Decimal Point: \033[0m"
                                               f"Stand-alone points "
                                               f"are not allowed.")
    return checked_expression
