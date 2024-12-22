def highlight_infix_error(infix_tokens, problematic_index):
    """
    Highlights the problematic token in the infix expression using its index.
    :param infix_tokens: List of tokens in infix notation.
    :type infix_tokens: list
    :param problematic_index: Index or range of indexes to highlight.
    :type problematic_index: int or tuple
    :return: Highlighted infix expression as a string.
    :rtype: str
    """
    highlighted_expression = ""
    for index, token in enumerate(infix_tokens):
        if isinstance(problematic_index, tuple):  # Represents a problematic index range to highlight
            if problematic_index[0] <= index <= problematic_index[1]:
                highlighted_expression += f"\033[91m\033[1m{token}\033[0m"
            else:
                highlighted_expression += str(token)
        elif index == problematic_index:  # Represents a single problematic index to highlight
            highlighted_expression += f"\033[91m\033[1m{token}\033[0m"
        else:
            highlighted_expression += str(token)
    return highlighted_expression
