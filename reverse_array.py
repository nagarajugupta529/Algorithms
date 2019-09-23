"""
here we have two methods to reverse an array with and without recursion
"""


def reverse(arr):
    """
    regular swapping method to reverse an array
    :param arr: list
    :return: reverse of list
    """
    n = len(arr)-1
    i = 0
    while i < n:
        arr[i], arr[n] = arr[n], arr[i]
        i = i + 1
        n = n-1
    return arr


def reverse_using_recursion(arr, start, end):
    """
    method to reverse an array using recursion
    :param arr: list
    :param start: int
    :param end: int
    :return: reverse of list
    """
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_using_recursion(arr, start+1, end-1)


if __name__ == "__main__":
    op = reverse_using_recursion([1, 2, 3, 4, 5, 6], 0, 5)
    print(op)
