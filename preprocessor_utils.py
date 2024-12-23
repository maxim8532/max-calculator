from calculator import Operator
from invalid_character_exception import InvalidCharacterException


def only_valid_characters_check(expression):
    """
    Checks if all the characters in the expression are valid for a mathematical expression.
    Highlights the invalid characters and raises an exception with details.
    :param expression: The expression before checking
    :type expression: str
    :return: The expression after being checked
    :rtype: str
    :raise InvalidCharacterException: if invalid characters appear in the expression
    """
    valid_special_characters = "()."
    expression_after_check = ""
    invalid_characters_list = []

    for char in expression:
        if not (char.isnumeric() or Operator.is_valid_operator(char) or char in valid_special_characters) or char == "u":
            if char not in invalid_characters_list:
                invalid_characters_list.append(char)
            expression_after_check += "\033[91m\033[1m" + char + "\033[0m"
            # Turns the invalid characters red and bold
        else:
            expression_after_check += char  # Adding a valid char
    if invalid_characters_list:
        expression_after_check.replace("u", "-")
        expression_after_check.replace("s", "-")
        raise InvalidCharacterException(f"{expression_after_check}\n\033[91mInvalid Characters: \033[0m"
                                        f"{invalid_characters_list}")  # Turns the message sent to the exception red
    else:
        return expression_after_check


def reduce_minuses(expression):
    """
    Reduces sequences of minus signs in an expression.

    :param expression: The mathematical expression
    :type expression: str
    :return: The reduced expression.
    :rtype: str
    """
    if not expression:  # Empty input
        return ""

    reduced_expression = ""
    is_minus_sequence = False  # Tracks if we are in a sequence of minuses
    current_sign_negative = True  # Tracks the current sign, toggles between True/False

    for index, char in enumerate(expression):
        if not is_minus_sequence:
            if char == "-" and (index == 0 or expression[index - 1] == "("
                                or Operator.is_valid_operator(expression[index - 1])):  # Start of sequence
                is_minus_sequence = True
            else:
                reduced_expression += char
        else:
            if char == "-":  # Extend minus sequence
                current_sign_negative = not current_sign_negative  # Toggle sign
            else:
                # End of minus sequence
                if current_sign_negative:
                    reduced_expression += "-" + char  # Add unary/sign minus
                else:
                    reduced_expression += char  # Positive sign, add character with no minuses
                is_minus_sequence = False  # Reset sequence tracking
    if is_minus_sequence and not reduced_expression:
        if current_sign_negative is True:
            return "-"  # If the only chars in the expression are minuses and their amount is odd

    return reduced_expression


def mark_special_minuses(expression):
    """
    Marks the unary and sign minuses.
    :param expression: The expression after the minuses have been reduced
    :type expression: str
    :return: The expression with the special minuses marked
    :rtype: str
    """
    marked_expression = ""
    for index, char in enumerate(expression):
        if char == "-" and (index == 0 or expression[index - 1] == "("):  # Unary minus
            marked_expression += "u"
        elif char == "-" and Operator.is_valid_operator(expression[index - 1]):  # Sign minus
            marked_expression += "s"
        else:
            marked_expression += char

    return marked_expression
