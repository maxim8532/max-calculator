from operators import Operator
from unary_operator import UnaryOperator
from binary_operator import BinaryOperator


class Calculator:
    def __init__(self):
        ...

    def preprocessor(self, expression):
        expression = expression.replace("", " ")  # Remove whitespaces
    @staticmethod
    def reduce_minuses(expression):
        """
        Reduces sequences of minus signs in an expression, distinguishing
        unary, binary, and sign minuses.

        :param expression: The mathematical expression
        :type expression: str
        :return: The reduced expression.
        :rtype: str
        """
        if not expression:  # Empty input
            return ""

        reduced_expression = ""
        is_minus_sequence = False  # Tracks if we are in a sequence of minuses
        is_sign_minus = False  # Tracks if the minus is a sign minus
        current_sign_negative = True  # Tracks the current sign, toggles between True/False

        for index, char in enumerate(expression):
            if not is_minus_sequence:
                if char == "-" and (index == 0 or expression[index - 1] == "("):  # Unary minus
                    is_minus_sequence = True
                elif char == "-" and Operator.is_valid_operator(expression[index - 1]):  # Sign minus
                    is_minus_sequence = True
                    is_sign_minus = True
                else:
                    reduced_expression += char  # Add non-minus characters
            else:
                if char == "-":  # Extend minus sequence
                    current_sign_negative = not current_sign_negative  # Toggle sign
                else:
                    # End of minus sequence
                    if current_sign_negative:
                        if is_sign_minus:
                            reduced_expression += "s" + char  # Add sign minus
                            is_sign_minus = False  # Reset
                        else:
                            reduced_expression += "u" + char  # Add unary minus
                    else:
                        reduced_expression += char  # Positive sign, add character with no minuses
                    is_minus_sequence = False  # Reset sequence tracking

        return reduced_expression


