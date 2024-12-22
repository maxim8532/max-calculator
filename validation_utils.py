import operators
from colors import Colors


def parentheses_check(token_list):
    """
    Checks for unmatched parentheses in a tokenized list and highlights all unmatched ones.
    :param token_list: List of tokens
    :type token_list: list
    :return: Tuple (check_passed, checked_expression)
    :rtype: tuple
    """
    stack = []
    checked_tokens = []

    # First for to check parentheses
    for index, token in enumerate(token_list):
        if token == "(" or token == "-(":
            stack.append(index)  # Store the index of unmatched "("
            checked_tokens.append(token)  # Add to final token list
        elif token == ")":
            if not stack:
                checked_tokens.append(
                    f"{Colors.BOLD}{Colors.FAIL}){Colors.ENDC}")  # Highlight unmatched closing parenthesis
            else:
                stack.pop()  # Match found, remove from stack
                checked_tokens.append(token)
        else:
            checked_tokens.append(str(token))

    # Second pass to highlight unmatched opening parentheses (if exists)
    for unmatched_index in stack:
        if checked_tokens[unmatched_index] == "(":
            # Check for sign minus before the parentheses and highlight accordingly
            checked_tokens[unmatched_index] = f"{Colors.BOLD}{Colors.FAIL}({Colors.ENDC}"
        else:
            # "-("
            checked_tokens[unmatched_index] = f"-{Colors.BOLD}{Colors.FAIL}({Colors.ENDC}"

    # Rebuild the expression to present to the user
    checked_expression = "".join(checked_tokens)

    # Checks if there are unmatched "(" in the stack or any ")" are highlighted
    if stack or Colors.FAIL in checked_expression:
        return False, checked_expression.replace("u", "-")
    else:
        return True, None


def binary_operators_between_valid_operands_check(token_list):
    """
    Checks for mis-placed binary operators and highlights them accordingly.
    :param token_list: The token list of the expression
    :type token_list: list
    :return: Tuple (check_passed, checked_expression)
    :rtype: tuple
    """
    checked_expression = ""  # The expression after the check, problematic operators will be highlighted

    for index, token in enumerate(token_list):
        next_token = token_list[index + 1] if index + 1 < len(token_list) else None
        prev_token = token_list[index - 1] if index > 0 else None

        if operators.Operator.is_valid_operator(token) and operators.Operator.get_type(token) == "binary":
            # Binary operators should be next to an expression, operand or a unary operator
            if ((next_token == "(" or next_token == "-(" or isinstance(next_token, float) or isinstance(next_token, int) or
                 (next_token is not None and operators.Operator.get_type(next_token) == "unary"
                 if operators.Operator.is_valid_operator(next_token) else False)) and
                    (prev_token == ")" or isinstance(prev_token, float) or isinstance(prev_token, int) or
                     (prev_token is not None and operators.Operator.get_type(prev_token) == "unary"
                     if operators.Operator.is_valid_operator(prev_token) else False))):

                checked_expression += str(token)
            else:
                checked_expression += f"{Colors.BOLD}{Colors.FAIL}{token}{Colors.ENDC}"  # Highlights the char in red
        else:
            checked_expression += str(token)  # Adding a non-binary operator token

    if Colors.FAIL in checked_expression:
        # Checks if there are any operators highlighted after the check.
        return False, checked_expression.replace("u", "-")
        # Did not pass the check, will return the expression with the problems in red
    else:
        return True, None  # Passed the check successfully


def negation_operator_next_to_number_check(token_list):
    """
    Checks for "~" operators that are not next to a number to their right.
    :param token_list: The token list of the expression
    :type token_list: list
    :return: Tuple (check_passed, checked_expression)
    :rtype: tuple
    """
    checked_expression = ""

    for index, token in enumerate(token_list):
        next_token = token_list[index + 1] if index + 1 < len(token_list) else None

        if token == "~" and not (isinstance(next_token, float) or isinstance(next_token, int)):
            # Checks if the token next to the "~" is a float number
            checked_expression += f"{Colors.BOLD}{Colors.FAIL}{token}{Colors.ENDC}"
        else:
            checked_expression += str(token)

    if Colors.FAIL in checked_expression:
        # If any token is highlighted, the check didn't pass
        return False, checked_expression
    else:
        # Check passed
        return True, None


def empty_parentheses_check(token_list):
    """
    Checks for empty parentheses and highlights them.
    :param token_list: The token list of the expression
    :type token_list: list
    :return: Tuple (check_passed, checked_expression)
    :rtype: tuple
    """
    string_expression = "".join(str(token) for token in token_list)  # Convert the token list to a string
    string_expression = string_expression.replace("()",
                                                 f"{Colors.BOLD}{Colors.FAIL}(){Colors.ENDC}")  # Highlight "()" if any

    if Colors.FAIL in string_expression:
        # If any token is highlighted, the check didn't pass
        return False, string_expression.replace("u", "-")
    else:
        # Check passed
        return True, None


def stand_alone_unary_operators_check(token_list):
    """
    Checks for stand alone unary operators and highlights them.
    :param token_list: The token list of the expression
    :type token_list: list
    :return: Tuple (check_passed, checked_expression)
    :rtype: tuple
    """
    checked_expression = ""

    for index, token in enumerate(token_list):
        next_token = token_list[index + 1] if index + 1 < len(token_list) else None
        prev_token = token_list[index - 1] if index > 0 else None

        # Unary operators can be next to a number, an expression or another number, relative to their position
        if operators.Operator.is_valid_operator(token) and operators.Operator.get_type(token) == "unary":
            if operators.Operator.get_position(token) == "right" and (  # Check if the position is "right"
                    (isinstance(prev_token, float) or isinstance(prev_token, int))  # Check for number next to it
                    or prev_token == ")"  # Check for end of an expression next to it
                    or (prev_token is not None and operators.Operator.get_type(prev_token) == "unary"
            if operators.Operator.is_valid_operator(prev_token) else False)):  # Check for unary operator

                checked_expression += str(token)

            elif operators.Operator.get_position(token) == "left" and (  # Check if the position is "left"
                    (isinstance(next_token, float) or isinstance(next_token, int))  # Check for number next to it
                    or next_token == "("  # Check for start of an expression next to it
                    or (next_token is not None and operators.Operator.get_type(next_token) == "unary"
            if operators.Operator.is_valid_operator(next_token) else False)):  # Check for unary operator

                checked_expression += str(token)

            else:
                checked_expression += f"{Colors.BOLD}{Colors.FAIL}{token}{Colors.ENDC}"  # Highlight the problematic operator
        else:
            checked_expression += str(token)

    if Colors.FAIL in checked_expression:
        # If any token is highlighted, the check didn't pass
        return False, checked_expression.replace("u", "-")
    else:
        # Check passed
        return True, None


def missing_operator_check(token_list):
    """
    Checks for missing operators between operands and expressions.
    :param token_list: The token list of the expression
    :type token_list: list
    :return: Tuple (check_passed, checked_expression)
    :rtype: tuple
    """
    checked_expression = ""

    for index, token in enumerate(token_list):
        next_token = token_list[index + 1] if index + 1 < len(token_list) else None
        prev_token = token_list[index - 1] if index > 0 else None

        is_right_unary_or_number_close = (
                token == ")" or
                (
                        operators.Operator.is_valid_operator(token) and
                        operators.Operator.get_type(token) == "unary" and
                        operators.Operator.get_position(token) == "right"
                ) or
                isinstance(token, float) or isinstance(token, int)
        )

        next_is_operand_or_left_unary = (
                next_token == "(" or
                isinstance(next_token, float) or isinstance(next_token, int) or
                (
                        operators.Operator.is_valid_operator(next_token) and
                        operators.Operator.get_type(next_token) == "unary" and
                        operators.Operator.get_position(next_token) == "left"
                )
        )

        cond1 = is_right_unary_or_number_close and next_is_operand_or_left_unary

        is_left_unary = (
                operators.Operator.is_valid_operator(token) and
                operators.Operator.get_type(token) == "unary" and
                operators.Operator.get_position(token) == "left"
        )
        prev_is_operand_or_right_unary_close = (
                prev_token == ")" or
                isinstance(prev_token, float) or isinstance(prev_token, int) or
                (
                        operators.Operator.is_valid_operator(prev_token) and
                        operators.Operator.get_type(prev_token) == "unary" and
                        operators.Operator.get_position(prev_token) == "right"
                )
        )

        cond2 = is_left_unary and prev_is_operand_or_right_unary_close

        if cond1 or cond2:
            # Highlight as a missing operator situation
            checked_expression += f"{token}{Colors.BOLD}{Colors.FAIL}|?|{Colors.ENDC}"
        else:
            checked_expression += str(token)

    if Colors.FAIL in checked_expression:
        return False, checked_expression.replace("u", "-")
    else:
        return True, None
