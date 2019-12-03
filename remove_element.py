def remove_element(nums, val):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == val:
            n = n-1
            num = nums.pop(i)
            nums.append(num)
        else:
            i+=1
    print nums
    return n


print(remove_element([1, 2, 3, 3, 3, 4, 5, 6],3))
