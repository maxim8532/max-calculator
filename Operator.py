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

    @staticmethod
    def get_operator_data(operator):
        """
        Retrieve data for a given operator from the operators' dictionary.
        :param operator: A given operator
        :type operator: str
        :return: A sub-dictionary for the operator key
        :rtype: dict

        """
        return Operator.operators_dict.get(operator)

    @staticmethod
    def get_type(operator):
        """
        Retrieve the type of operator (unary or binary).
        :param operator: A given operator
        :type operator: str
        :return: The type of the operator
        :rtype: str
        """
        operator_data = Operator.get_operator_data(operator)
        return operator_data["type"]

    @staticmethod
    def get_priority(operator):
        """
        Retrieve the priority of an operator.
        :param operator: A given operator
        :type operator: str
        :return: The priority of an operator
        :rtype: int
        """
        operator_data = Operator.get_operator_data(operator)
        return operator_data["priority"]

    @staticmethod
    def get_position(operator):
        """
        Retrieve the position of an operator relative to the operand/s next to it
        :param operator: A given operator
        :type operator: str
        :return: The position
        :rtype: str
        """
        operator_data = Operator.get_operator_data(operator)
        return operator_data["position"]

    @staticmethod
    def get_operation(operator):
        """
        Retrieve a reference to a method which the operator perform
        :param operator: A given operator
        :type operator: str
        :return: The operation method
        :rtype: Callable
        """
        operator_data = Operator.get_operator_data(operator)
        return operator_data["operation"]
