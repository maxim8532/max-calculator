from abc import ABC

from BinaryOperator import BinaryOperator
from UnaryOperator import UnaryOperator


class Operator(ABC):
    """
    An abstract class with an attribute of an operation priorities dictionary where
    every operator has its own dictionary which contains his essential attributes.

    Attributes:
        operators_dict: A dictionary for mathematical operations that contains attributes
            like -  the type of the operation (binary or unary).
            the priority of the operator (operators with a higher priority value will be used first).
            the position of the operator compared to the operand/s.
            and the operation which references a static method that executes the operation.
    """
    operators_dict = {
        "+": {
            "type": "binary",
            "priority": 1,
            "position": "middle",
            "operation": BinaryOperator.add
        },  # plus
        "-": {
            "type": "binary",
            "priority": 1,
            "position": "middle",
            "operation": BinaryOperator.subtract
        },  # minus
        "*": {
            "type": "binary",
            "priority": 2,
            "position": "middle",
            "operation": BinaryOperator.multiply
        },  # multiply
        "/": {
            "type": "binary",
            "priority": 2,
            "position": "middle",
            "operation": BinaryOperator.divide
        },  # divide
        "u": {
            "type": "unary",
            "priority": 3,
            "position": "left",
            "operation": UnaryOperator.negative
        },  # unary minus
        "^": {
            "type": "binary",
            "priority": 4,
            "position": "middle",
            "operation": BinaryOperator.power
        },  # power
        "%": {
            "type": "binary",
            "priority": 5,
            "position": "middle",
            "operation": BinaryOperator.modulo
        },  # modulo
        "$": {
            "type": "binary",
            "priority": 6,
            "position": "middle",
            "operation": BinaryOperator.max
        },  # max
        "&": {
            "type": "binary",
            "priority": 6,
            "position": "middle",
            "operation": BinaryOperator.min
        },  # min
        "@": {
            "type": "binary",
            "priority": 6,
            "position": "middle",
            "operation": BinaryOperator.avg
        },  # avg
        "~": {
            "type": "unary",
            "priority": 7,
            "position": "left",
            "operation": UnaryOperator.negative
        },  # negation
        "!": {
            "type": "unary",
            "priority": 7,
            "position": "right",
            "operation": UnaryOperator.factorial
        },  # factorial
        "#": {
            "type": "unary",
            "priority": 7,
            "position": "right",
            "operation": UnaryOperator.hashtag
        }  # hashtag
    }

