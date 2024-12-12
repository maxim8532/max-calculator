import Operator
from math import pow


class BinaryOperator(Operator):
    """
        A class that extends the Operator class.
        provides static methods for binary mathematical operations.

        :type methods: staticmethod

        Methods:
            add(left_operand, right_operand): Perform addition
            subtract(left_operand, right_operand): Perform subtraction
            multiply(left_operand, right_operand): Perform multiplication
            divide(left_operand, right_operand): Perform division
            power(left_operand_base, right_operand_power): Perform exponentiation
            modulo(left_operand, right_operand): Perform modulo operation
            max(left_operand, right_operand): Find maximum value
            min(left_operand, right_operand): Find minimum value
            avg(left_operand, right_operand): Find average value
        """
    @staticmethod
    def add(left_operand, right_operand):
        return left_operand + right_operand

    @staticmethod
    def subtract(left_operand, right_operand):
        return left_operand - right_operand

    @staticmethod
    def multiply(left_operand, right_operand):
        return left_operand * right_operand

    @staticmethod
    def divide(left_operand, right_operand):
        return left_operand / right_operand

    @staticmethod
    def power(left_operand_base, right_operand_power):
        return pow(left_operand_base, right_operand_power)

    @staticmethod
    def modulo(left_operand, right_operand):
        return left_operand % right_operand

    @staticmethod
    def max(left_operand, right_operand):
        return max(left_operand, right_operand)

    @staticmethod
    def min(left_operand, right_operand):
        return min(left_operand, right_operand)

    @staticmethod
    def avg(left_operand, right_operand):
        return (left_operand + right_operand) / 2
