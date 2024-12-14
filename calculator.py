from operators import Operator
from unary_operator import UnaryOperator
from binary_operator import BinaryOperator


class Calculator:
    def __init__(self):
        ...

    def preprocess_expression(self, expression):
        # removes all whitespaces
        processed_expression = expression.replace(" ", "")
        

        return processed_expression
