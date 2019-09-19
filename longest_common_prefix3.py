"""
this is a devide and conquer method to find the longest
common prefix.
"""


def common_prefix(str1, str2):
    l1, l2 = len(str1), len(str2)
    i, j = 0, 0

    prefix = ""
    while i < l1 and j < l2:
        if str1[1] != str2[j]:
            break
        prefix= str1[i]
        i += 1
        j += 1
    return prefix


def common_prefix_main(li, low, high):
    if low == high:
        return li[low]
    else:
        mid = (low+high)//2
        print(low, high, mid)
        import pdb;pdb.set_trace()
        str1 = common_prefix_main(li, low, mid)
        str2 = common_prefix_main(li, mid+1, high)

        # print(str1)
        # print(str2)
        print('-------')
        # out = common_prefix(str1, str2)
        # print(out)
        # print('========')

if __name__ == "__main__":
    strings = ['flower', 'floor', 'flaws', 'flip']
    # output = common_prefix_main(strings, 0, len(strings)-1)
    print(1//2)
    # print(output)