
class UnaryOperator:
    """
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
        operand = int(operand)
        factorial_sum = 1
        for number in range(1, operand + 1):
            factorial_sum *= number
        return float(factorial_sum)

    @staticmethod
    def hashtag(operand):
        """
        Calculates the sum of the digits of a given operand
        :param operand:  A given operand
        :type operand: int, float
        :return: the sum of the operand's digits
        :rtype: int
        """
        # Handle float operands
        operand = int(str(operand).replace(".", ""))
        hashtag_sum = 0
        while operand != 0:
            hashtag_sum += operand % 10
            operand //= 10
        return hashtag_sum
