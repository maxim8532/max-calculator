from abc import ABC


class Operator(ABC):
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
