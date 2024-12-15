from operators import Operator
from unary_operator import UnaryOperator
from binary_operator import BinaryOperator


class Calculator:
    def __init__(self, expression):
        self._expression = expression

    def preprocessor(self):
        expression = self._expression.replace(" ", "")  # Remove whitespaces
        expression = self.reduce_minuses(expression)
        expression = self.mark_special_minuses(expression)
        return expression

    @staticmethod
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

        return reduced_expression

    @staticmethod
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
