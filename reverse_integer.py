def reverse(n):
    neg_flag = None
    if n > (2**31-1) or n < (-2**31):
        return 0
    if n < 0:
        neg_flag = True
        n = n*-1
    n = str(n)
    n = n[len(n)::-1]
    n = int(n)
    if n > (2**31-1):
        return 0
    if neg_flag:
        return -1*n
    return n


print(reverse(1534236469))
