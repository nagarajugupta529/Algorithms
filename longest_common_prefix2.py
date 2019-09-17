"""
this is a character based method to find the longest
common prefix.
"""


def find_minimum_length(li):
    """
    returns the min string length from list
    :param li: list of strings
    :return: int
    """
    current = li[0]
    for i in range(1, len(li)):
        if len(current) > len(li[i]):
            current = li[i]
    return len(current)


def common_prefix_main(li):
    """
    returns the longest common prefix
    :param li: ist of strings
    :return: str
    """
    min_string_length = find_minimum_length(li)
    result = ""
    for i in range(min_string_length):
        current = li[0][i]
        for j in range(1, len(li)):
            if not current == li[j][i]:
                return result
        result = result + current
    return result


if __name__ == "__main__":
    strings = ['flower', 'floor', 'flows', 'fl']
    output = common_prefix_main(strings)
    print(output)
