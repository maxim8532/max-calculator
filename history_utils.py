from colors import Colors


def add_to_history(history_list, expression, result):
    """
    Adds a successfully calculated expression and its result to the history.
    Keeps only the 5 most recent entries.
    :param history_list: the list that contains the current history
    :param expression: The evaluated expression.
    :param result: The result of the evaluated expression.
    """
    history_list.append((expression, result))
    if len(history_list) > 5:
        history_list.pop(0)  # Remove the oldest entry to maintain a maximum of 5 items.


def display_history(history_list):
    """
    Displays the 5 most recent expressions and their results.
    :param history_list: the list that contains the current history
    """
    if not history_list:
        print(f"{Colors.CYAN}History is empty!{Colors.ENDC}")
    else:
        print(f"\n{Colors.BLUE}Recent Calculations:{Colors.ENDC}")
        for i, (exp, res) in enumerate(history_list, start=1):
            print(f"{Colors.BOLD}{i}) {exp} = {res}{Colors.ENDC}")