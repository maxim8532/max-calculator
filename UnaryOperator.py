import Operator


class UnaryOperator(Operator):

    @staticmethod
    def negative(operand):
        return -operand

    @staticmethod
    def factorial(operand):
        factorial_sum = 1
        for number in range(1, operand + 1):
            factorial_sum *= number
        return factorial_sum
