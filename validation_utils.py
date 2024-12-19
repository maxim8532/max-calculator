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
            if ((next_token == "(" or isinstance(next_token, float) or
                operators.Operator.get_type(next_token) == "unary") and
                (prev_token == ")" or isinstance(prev_token, float) or
                 (operators.Operator.get_type(prev_token) == "unary"))):

                checked_expression += str(token)
            else:
                checked_expression += f"\033[91m\033[1m{token}\033[0m"  # Highlights the char in red
        else:
            checked_expression += str(token)

    if "\033[91m" in checked_expression:
        # Checks if there are any operators highlighted after the check.
        return False, checked_expression  # Did not pass the check, will return the expression with the problems in red
    else:
        return True, None  # Passed the check successfully
