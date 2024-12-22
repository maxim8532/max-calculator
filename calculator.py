from invalid_character_exception import InvalidCharacterException
from invalid_decimal_point_exception import InvalidDecimalPointException
from invalid_expression_exception import InvalidExpressionException
from operators import Operator
import preprocessor_utils
import tokenization_utils
import validation_utils
import postfix_evaluation_utils
import history_utils
from colors import Colors


class Calculator:
    """
        A class representing a mathematical expression evaluator with preprocessing, validation,
        infix-to-postfix conversion, and postfix evaluation steps.

        Attributes:
            _expression (str or list): The mathematical expression to evaluate, initially in string form and
                tokenized as a list during processing.
            _postfix_expression (list): The expression converted into postfix notation for evaluation.
            history (list): The 5 most recent expressions calculated.

        Methods:
            __init__(expression):
                Initializes the Calculator instance with a mathematical expression.

            preprocessor():
                Preprocesses the input expression to prepare it for tokenization and validation.
                - Removes whitespace.
                - Checks for invalid characters.
                - Reduces sequences of minuses.
                - Marks special minuses (unary and sign).

            tokenization():
                Converts the preprocessed expression into a list of tokens (numbers and operators).
                - Ensures valid placement of decimal points.
                - Handles negative numbers.

            validation():
                Validates the tokenized expression against predefined rules:
                - Ensures parentheses are balanced and used correctly.
                - Prevents empty parentheses.
                - Checks the proper placement of binary and unary operators.
                - Validates negation operator placement.
                - Ensures no missing operators between operands.

            infix_to_postfix():
                Converts the validated infix expression to postfix notation while preserving token indexes.
                - Maintains operator priority and position.
                - Handles special cases like "-(" for unary minus.

            evaluate_postfix():
                Evaluates the postfix expression and returns the calculated result.
                - Performs error handling for division by zero.
                - Validates factorials and hashtags (custom operators) for valid input.

            calculate():
                The main calculation method that combines all the steps:
                - Preprocessing, tokenization, validation, conversion, and evaluation.
                - Handles exceptions such as invalid expressions, division by zero, and overflow errors.
        """
    expression_history = []

    def __init__(self, expression):
        self._expression = expression
        self._postfix_expression = None

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
            if not expression:
                # Empty expression
                self._expression = None
                print(f"\n{Colors.WARNING}\033[1mEmpty Expression.{Colors.ENDC}")
            else:
                self._expression = expression
        except InvalidCharacterException as e:
            valid_operators_list = list(Operator.get_operators_keys())
            valid_operators_list.remove('u')  # mark for unary minus, should not be inserted by user
            print(
                f"{e} \n{Colors.GREEN}Valid Characters:{Colors.ENDC} numbers (Integer and decimal), brackets () and operators: "
                f"{valid_operators_list}")
            self._expression = None
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
                        number = float(current_token)
                        if number.is_integer():
                            token_list.append(int(current_token))
                        else:
                            token_list.append(number)  # Add a float token
                        current_token = ""  # Reset for next token
                elif char == ".":
                    current_token += char
                    if next_char:
                        if not next_char.isdecimal():
                            token_list.append(float(current_token))
                            current_token = ""
                elif char == "s":  # Handle sign minus
                    current_token += "-"
                else:
                    current_token += char
                    token_list.append(current_token)
                    current_token = ""  # Add operator or special character

            # Add any remaining token at the end
            if current_token:
                token_list.append(float(current_token))
            self._expression = token_list
        except InvalidDecimalPointException as e:
            print(f"{e} \n{Colors.GREEN}Valid Placement of Decimal Point: {Colors.ENDC}(0).123, 1.23, 123.(0)")
            self._expression = None  # Expression is not valid

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
        6. Check for missing operators between operands

        :return: The error message showing the user every error highlighted in red
        :rtype: str
        """
        error_message = ""

        # 1. Check for balanced parentheses
        check_passed, error_expression = validation_utils.parentheses_check(self._expression)
        if not check_passed:
            error_message += (f"\n\n{error_expression}\n{Colors.FAIL}Invalid Expression: {Colors.ENDC}"
                              f"Parentheses are not balanced.")

        # 2. Check for empty parentheses
        check_passed, error_expression = validation_utils.empty_parentheses_check(self._expression)
        if not check_passed:
            error_message += (f"\n\n{error_expression}\n{Colors.FAIL}Invalid Expression: {Colors.ENDC}"
                              f"Empty parentheses are not allowed.")

        # 3. Check binary operator placement
        check_passed, error_expression = validation_utils.binary_operators_between_valid_operands_check(
            self._expression)
        if not check_passed:
            error_message += (f"\n\n{error_expression}\n{Colors.FAIL}Invalid Expression: {Colors.ENDC}"
                              f"Binary operators should be between two operands or expressions.")

        # 4. Check negation operator placement
        check_passed, error_expression = validation_utils.negation_operator_next_to_number_check(self._expression)
        if not check_passed:
            error_message += (f"\n\n{error_expression}\n{Colors.FAIL}Invalid Expression: {Colors.ENDC}"
                              f"Negation operator (~) should only be next to a number.")

        # 5. Check for stand-alone unary operators
        check_passed, error_expression = validation_utils.stand_alone_unary_operators_check(self._expression)
        if not check_passed:
            error_message += (f"\n\n{error_expression}\n{Colors.FAIL}Invalid Expression: {Colors.ENDC}"
                              f"Unary operators cannot be stand-alone.")

        # 6. Check for missing operators between operands
        check_passed, error_expression = validation_utils.missing_operator_check(self._expression)
        if not check_passed:
            error_message += (f"\n\n{error_expression}\n{Colors.FAIL}Invalid Expression: {Colors.ENDC}"
                              f"There are some missing operators.")
        if error_message:
            self._expression = None
            raise InvalidExpressionException(f"\n{error_message}")

    def infix_to_postfix(self):
        """
        Converts an infix expression to postfix notation while preserving token indexes to present them
        in an error message later if needed in a convenient way.
        """
        token_list = self._expression
        output = []
        operator_stack = []

        for index, token in enumerate(token_list):
            if isinstance(token, float) or isinstance(token, int):  # Numbers go directly to the output
                output.append((token, index))
            elif token == "(":
                operator_stack.append((token, index))
            elif token == ")":
                # Pop until matching opening parenthesis
                while operator_stack and operator_stack[-1][0] != "(":
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Remove the opening parenthesis

                # Check if a sign minus ("s") is in the stack
                if operator_stack and operator_stack[-1][0] == "s":
                    output.append(operator_stack.pop())
            elif token == "-(":
                # Treat "-(" as a signal for sign minus
                operator_stack.append(("s", index))
                operator_stack.append(("(", index))
            elif Operator.is_valid_operator(token):
                # Handle valid operators based on priority and position
                while (operator_stack and operator_stack[-1][0] != "(" and
                       (Operator.get_priority(operator_stack[-1][0]) > Operator.get_priority(token) or
                        (Operator.get_priority(operator_stack[-1][0]) == Operator.get_priority(token) and
                         Operator.get_position(token) != "right"))):
                    output.append(operator_stack.pop())
                operator_stack.append((token, index))

        # Pop all remaining operators in the stack
        while operator_stack:
            output.append(operator_stack.pop())

        self._postfix_expression = output

    def evaluate_postfix(self):
        """
        Evaluates the postfix expression.
        :return: The result of the evaluated expression.
        :rtype: float
        :raises ValueError: If the postfix expression is invalid or contains runtime errors.
        :raises ZeroDivisionError: when a division by zero occurs.
        """
        stack = []

        for token, index in self._postfix_expression:
            if isinstance(token, float) or isinstance(token, int):  # Operands
                stack.append((token, index))
            elif Operator.is_valid_operator(token):  # Operators
                operator_type = Operator.get_type(token)
                operation = Operator.get_operation(token)

                if operator_type == "binary":
                    # Binary operator requires two operands
                    try:
                        right_operand, right_index = stack.pop()
                        left_operand, left_index = stack.pop()
                    except IndexError:  # Incase the checks somehow don't catch it before
                        raise ValueError("Invalid postfix expression: insufficient operands for binary operator.")

                    # Division by zero check
                    if token == "/" and right_operand == 0:
                        highlighted_expression = postfix_evaluation_utils.highlight_infix_error(
                            self._expression, (right_index - 1, right_index)).replace("u", "-")  # highlights the "/0"
                        raise ZeroDivisionError(f"\n{highlighted_expression}\n{Colors.FAIL}Zero Division Error: "
                                                f"{Colors.ENDC}Division by zero is not allowed.")

                    # Perform the operation
                    result = operation(left_operand, right_operand)
                    combined_index = (left_index, right_index)
                    stack.append((result, combined_index))

                elif operator_type == "unary":
                    # Unary operator requires one operand
                    try:
                        operand, operand_index = stack.pop()
                    except IndexError:  # Incase the checks somehow don't catch it before
                        raise ValueError("Invalid postfix expression: insufficient operand for unary operator.")

                    if token == "!" and (operand < 0 or not (operand == int(operand)) or operand > 170):
                        highlighted_expression = postfix_evaluation_utils.highlight_infix_error(
                            self._expression, (operand_index, operand_index + 1)).replace("u", "-")
                        # highlights the "{operand}!"
                        raise ValueError(
                            f"\n{highlighted_expression}\n{Colors.FAIL}Value Error: {Colors.ENDC}"
                            f"Factorial is only defined for non-negative integers up to 170.")

                    if token == "#" and operand < 0:
                        highlighted_expression = postfix_evaluation_utils.highlight_infix_error(
                            self._expression, (operand_index, operand_index + 1)).replace("u", "-")
                        # highlights the "{operand}#"
                        raise ValueError(
                            f"\n{highlighted_expression}\n{Colors.FAIL}Value Error: {Colors.ENDC}"
                            f"Hashtag is only defined for non-negative numbers")

                    # Perform the operation
                    result = operation(operand)
                    stack.append((result, operand_index))

        # Final validation
        if len(stack) != 1:
            # Incase the checks somehow don't catch it before
            raise ValueError("Invalid postfix expression: too many operands or insufficient operators.")

        return stack[0][0]  # Return only the result

    def calculate(self):
        """
        The final step the calculates the expression if all the steps before were completed.
        """
        try:
            Calculator.preprocessor(self)
            if self._expression is not None:
                Calculator.tokenization(self)
            if self._expression is not None:
                Calculator.validation(self)
            if self._expression is not None:
                Calculator.infix_to_postfix(self)
            if self._expression is not None:
                result = float(Calculator.evaluate_postfix(self))
                if result.is_integer():
                    result = int(result)
                print(f"{Colors.GREEN}Result:{Colors.ENDC} {result}")
                # Add to history only if calculation is successful
                expression_str = " ".join(map(str, self._expression))
                history_utils.add_to_history(Calculator.expression_history, expression_str, result)
                return result
        except InvalidExpressionException as e:
            print(f"{e}")
        except ValueError as e:
            print(f"{e}")
        except ZeroDivisionError as e:
            print(f"{e}")
        except TypeError as e:
            # If something in the checks goes terrible
            print(f"{e}")
        except OverflowError:
            print(f"\n{Colors.WARNING}Calculation is too big for the calculator to handle!{Colors.ENDC}")
        except MemoryError:
            # Just for safety :)
            print(
                f"\n{Colors.WARNING}Calculation exceeds available memory. Please simplify your expression.{Colors.ENDC}")
