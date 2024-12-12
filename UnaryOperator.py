import Operator


class UnaryOperator(Operator):
    """
    A class that extends the Operator abstract class.
    provides static methods for unary mathematical operations.

    :type methods: staticmethod

    Methods:
        negative(operand): Perform negation operation
        factorial(operand): Perform factorial operation
    """
    @staticmethod
    def negative(operand):
        return -operand

    @staticmethod
    def factorial(operand):
        """
        Calculates the factorial value of a given operand
        :param operand: A given operand
        :type operand: int
        :return: The factorial value of the given operand
        :rtype: int
        :raise ValueError: The factorial operation is only defined for non-negative integers
        """
        if not isinstance(operand, int) or operand < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        factorial_sum = 1
        for number in range(1, operand + 1):
            factorial_sum *= number
        return factorial_sum
