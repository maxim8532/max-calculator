from abc import ABC


class Operator(ABC):
    """
    An abstract class with an attribute of an operation priorities dictionary

    Attributes:
        operator_priorities_dict: A priorities dictionary for mathematical operations
    """
    operator_priorities_dict = {"+": 1,
                                "-": 1,
                                "*": 2,
                                "/": 2,
                                "u": 3,
                                "^": 4,
                                "%": 5,
                                "$": 6,
                                "&": 6,
                                "@": 6,
                                "~": 7,
                                "!": 7}
