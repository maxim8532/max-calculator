import operators


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
        if token == "(":
            stack.append(index)  # Store the index of unmatched "("
            checked_tokens.append(token)  # Add to final token list
        elif token == ")":
            if not stack:
                checked_tokens.append("\033[91m\033[1m)\033[0m")  # Highlight unmatched closing parenthesis
            else:
                stack.pop()  # Match found, remove from stack
                checked_tokens.append(token)
        else:
            checked_tokens.append(str(token))

    # Second pass to highlight unmatched opening parentheses (if exists)
    for unmatched_index in stack:
        checked_tokens[unmatched_index] = "\033[91m\033[1m(\033[0m"

    # Rebuild the expression to present to the user
    checked_expression = "".join(checked_tokens)

    # Checks if there are unmatched "(" in the stack or any ")" are highlighted
    if stack or "\033[91m" in checked_expression:
        return False, checked_expression
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
            if ((next_token == "(" or next_token == "-(" or isinstance(next_token, float) or
                 (next_token is not None and operators.Operator.get_type(next_token) == "unary"
                 if operators.Operator.is_valid_operator(next_token) else False)) and
                    (prev_token == ")" or isinstance(prev_token, float) or
                     (prev_token is not None and operators.Operator.get_type(prev_token) == "unary"
                     if operators.Operator.is_valid_operator(prev_token) else False))):

                checked_expression += str(token)
            else:
                checked_expression += f"\033[91m\033[1m{token}\033[0m"  # Highlights the char in red
        else:
            checked_expression += str(token)  # Adding a non-binary operator token

    if "\033[91m" in checked_expression:
        # Checks if there are any operators highlighted after the check.
        return False, checked_expression  # Did not pass the check, will return the expression with the problems in red
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

        if token == "~" and not isinstance(next_token, float):
            # Checks if the token next to the "~" is a float number
            checked_expression += f"\033[91m\033[1m{token}\033[0m"
        else:
            checked_expression += str(token)

    if "\033[91m" in checked_expression:
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
    string_expression = string_expression.replace("()", "\033[91m\033[1m()\033[0m")  # Highlight "()" if any

    if "\033[91m" in string_expression:
        # If any token is highlighted, the check didn't pass
        return False, string_expression
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
                    isinstance(prev_token, float)  # Check for float number next to it
                    or prev_token == ")"  # Check for end of an expression next to it
                    or (prev_token is not None and operators.Operator.get_type(prev_token) == "unary"
                        if operators.Operator.is_valid_operator(prev_token) else False)):  # Check for unary operator

                checked_expression += str(token)

            elif operators.Operator.get_position(token) == "left" and (  # Check if the position is "left"
                    isinstance(next_token, float)  # Check for float number next to it
                    or next_token == "("  # Check for start of an expression next to it
                    or (next_token is not None and operators.Operator.get_type(next_token) == "unary"
                        if operators.Operator.is_valid_operator(next_token) else False)):  # Check for unary operator

                checked_expression += str(token)

            else:
                checked_expression += f"\033[91m\033[1m{token}\033[0m"  # Highlight the problematic operator
        else:
            checked_expression += str(token)

    if "\033[91m" in checked_expression:
        # If any token is highlighted, the check didn't pass
        return False, checked_expression
    else:
        # Check passed
        return True, None
