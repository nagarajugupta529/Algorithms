"""
Popular Way of Finding the fibonacci series

Fibonacci Series : 0 1 1 2 3 5 8 13 21 34......
"""


def fibonacci(n):
    """
    Finding the Nth Fibonacci number using recursion
    :param n: integer
    :return: integer
    formula: F(n) = F(n-1) + F(n-2)
        * F(0) = 0
        * F(1) = 1
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    op = fibonacci(9)
    print(op)
