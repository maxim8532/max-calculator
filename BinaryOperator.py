import Operator
from math import pow


class BinaryOperator(Operator):

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
    