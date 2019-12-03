"""
this is a devide and conquer method to find the longest
common prefix.
"""


def common_prefix(str1, str2):
    l1, l2 = len(str1), len(str2)
    i, j = 0, 0

    common_string = ""
    while i < l1 and j < l2:
        if str1[i] != str2[j]:
            break
        common_string = common_string + str1[i]
        i += 1
        j += 1
    return common_string


def common_prefix_main(input_list, low, high):
    if low == high:
        return input_list[low]
    else:
        mid = (low+high)//2
        str1 = common_prefix_main(input_list, low, mid)
        str2 = common_prefix_main(input_list, mid+1, high)

        return common_prefix(str1, str2)

if __name__ == "__main__":
    strings = ['flower', 'floor', 'flows', 'flop']
    output = common_prefix_main(strings, 0, len(strings)-1)
    print(output)