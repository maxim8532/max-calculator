from invalid_character_exception import InvalidCharacterException
from invalid_decimal_point_exception import InvalidDecimalPointException
from operators import Operator
import preprocessor_utils
import tokenization_utils
import validation_utils
from unary_operator import UnaryOperator
from binary_operator import BinaryOperator


class Calculator:
    def __init__(self, expression):
        self._expression = expression

    def preprocessor(self):
        """
        Preprocesses the mathematical expression, gets it ready for the next step.

        Steps:
        1. Removes whitespaces.
        2. Checks for invalid characters.
        3. Reduces minus sequences.
        4. Marks special minuses (unary and sign).

        :raises InvalidCharacterException: If invalid characters are found.
        """
        expression = self._expression
        try:
            expression = self._expression.replace(" ", "")  # Remove whitespaces
            expression = preprocessor_utils.only_valid_characters_check(expression)
            # Check if the expression is valid, else raise an exception
            expression = preprocessor_utils.reduce_minuses(expression)  # Reduce the number of minuses
            expression = preprocessor_utils.mark_special_minuses(expression)  # Marks unary and sign minuses
            self._expression = expression
            print(expression)
        except InvalidCharacterException as e:
            print(f"{e} \n\033[92mValid Characters:\033[0m numbers (Integer and decimal), brackets () and operators: "
                  f"{list(Operator.get_operators_keys())}")
            self._expression = ""
            # Prints the valid characters explanation in green

    def tokenization(self):
        """
        Tokenizes the preprocessed expression into a list of numbers and operators.
        Validates decimal point usage before tokenization.

        :raises InvalidDecimalPointerException: if the validation of the decimal points placement fails.
        """
        if not self._expression:
            return []

        # Validate and mark decimal points
        try:
            validated_expression = tokenization_utils.decimal_point_check(self._expression)

            # Tokenization process
            token_list = []
            current_token = ""
            processed_expression = validated_expression

            for index, char in enumerate(processed_expression):
                next_char = processed_expression[index + 1] if index + 1 < len(processed_expression) else None

                if char.isdecimal():
                    current_token += char
                    if not (next_char and (next_char.isdecimal() or next_char == ".")):
                        token_list.append(float(current_token))  # Add a float token
                        current_token = ""  # Reset for next token
                elif char == ".":
                    current_token += char
                    if next_char:
                        if not next_char.isdecimal():
                            token_list.append(float(current_token))
                            current_token = ""
                elif char == "s":  # Handle sign minus  FIXME: missing check if next operand is decimal or dot
                    current_token += "-"
                else:
                    current_token += char
                    token_list.append(current_token)
                    current_token = ""  # Add operator or special character

            # Add any remaining token at the end
            if current_token:
                token_list.append(float(current_token))
            self._expression = token_list
            return token_list
        except InvalidDecimalPointException as e:
            print(f"{e} \n\033[92mValid Placement of Decimal Point: \033[0m(0).123, 1.23, 123.(0)")
            self._expression = []  # Expression is not valid

    def validation(self):
        """
        A validation step to catch errors that don't follow the rules that should be in every valid expression.
        The validation step highlights the errors and presents them to the user if needed.

        The steps in the validation process:
        1. Check for balanced parentheses
        2. Check for empty parentheses
        3. Check binary operator placement
        4. Check negation operator placement
        5. Check for stand-alone unary operators

        :return: The error message showing the user every error highlighted in red
        :rtype: str
        """
        error_message = ""

        # 1. Check for balanced parentheses
        check_passed, error_expression = validation_utils.parentheses_check(self._expression)
        if not check_passed:
            error_message += f"\n{error_expression}\nParentheses are not balanced."

        # 2. Check for empty parentheses
        check_passed, error_expression = validation_utils.empty_parentheses_check(self._expression)
        if not check_passed:
            error_message += f"\n{error_expression}\nEmpty parentheses are not allowed."

        # 3. Check binary operator placement
        check_passed, error_expression = validation_utils.binary_operators_between_valid_operands_check(
            self._expression)
        if not check_passed:
            error_message += f"\n{error_expression}\nBinary operators should be between two operands or expressions."

        # 4. Check negation operator placement
        check_passed, error_expression = validation_utils.negation_operator_next_to_number_check(self._expression)
        if not check_passed:
            error_message += f"\n{error_expression}\nNegation operator (~) should be next to a number on its right."

        # 5. Check for stand-alone unary operators
        check_passed, error_expression = validation_utils.stand_alone_unary_operators_check(self._expression)
        if not check_passed:
            error_message += f"\n{error_expression}\nUnary operators cannot be stand-alone."

        # Return errors if any were found
        if error_message:
            return error_message
        else:
            return self._expression

