"""
this is a word based method to find the longest
common prefix.
"""


def return_prefix(str1, str2):
    """
    compares two strings and returns common prefix
    :param str1: string1
    :param str2: string2
    :return: string
    """
    l1 = len(str1)
    l2 = len(str2)
    i, j = 0, 0
    prefix = ''
    while i < l1 and j < l2:
        if str1[i] != str2[j]:
            break
        prefix = prefix+str1[i]
        i = i+1
        j = j+1
    return prefix


def common_prefix_main(li):
    """
    :param li: list of strings
    :return: longest common prefix <str>
    """
    prefix = li[0]
    for i in range(1, len(li)):
        prefix = return_prefix(prefix, li[i])
    return prefix


if __name__ == "__main__":
    strings = ['flower', 'floor', 'flaws']
    output = common_prefix_main(strings)
    print(output)
