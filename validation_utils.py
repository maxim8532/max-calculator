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
        return True, checked_expression
