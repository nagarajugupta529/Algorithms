"""
Popular Ways of Finding the Factorial without using <<<math>>>

Factorial Formula : n! = n * (n-1) * (n-2) * (n-3) * (n-4) * ....... * 1
**1! == 0! == 1**
"""


def factorial_recursion(n):
    """
    Finding the Factorial of a given integer Using the Recursion Mechanism
    :param n: integer
    :return: integer
    """
    if n < 0:
        print('Factorial is Not exist For Negative False')
        return False
    if n == 0:
        return 1
    else:
        return n*factorial_recursion(n-1)


def factorial_using_for_loop(n):
    """
    Finding the Factorial of a given integer Using Simple for loop
    :param n: integer
    :return: integer
    """
    if n < 0:
        print('Factorial is Not Exist For Negative False')
        return False
    if n == 0:
        return 1
    val = 1
    for i in range(n, 0, -1):
        val = val * i
    return val


if __name__ == "__main__":
    op = factorial_using_for_loop(1)
    print(op)
    op = factorial_recursion(5)
    print(op)
