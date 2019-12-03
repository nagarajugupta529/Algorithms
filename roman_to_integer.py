def roman_to_int(string):
    global_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    n = len(string)
    res = global_dict[string[-1]]
    for i in range(n-1):
        if global_dict[string[i]] < global_dict[string[i+1]]:
            res = res - global_dict[string[i]]
        if global_dict[string[i]] >= global_dict[string[i+1]]:
            res = res + global_dict[string[i]]
    return (res)

