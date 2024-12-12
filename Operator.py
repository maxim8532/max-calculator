from abc import ABC


class Operator(ABC):
    """
    An abstract class with an attribute of an operation priorities dictionary

    Attributes:
        operator_priorities_dict: A priorities dictionary for mathematical operations.
        Operators with a higher priority value will be used first.
    """
    operator_priorities_dict = {
        "+": 1,  # plus
        "-": 1,  # minus
        "*": 2,  # multiply
        "/": 2,  # divide
        "u": 3,  # This operator represents a unary minus
        "^": 4,  # power
        "%": 5,  # modulo
        "$": 6,  # max
        "&": 6,  # min
        "@": 6,  # avg
        "~": 7,  # negative
        "!": 7,  # factorial
        "#": 7  # hashtag
    }
