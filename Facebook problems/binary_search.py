def binary_search(num, lst):
    lst.sort()
    lgt = len(lst)
    upper = lst[lgt-1]
    lower = lst[0]
    mid = lst[(upper-lower)//2]
    while mid != num:
        if mid == 0:
            return False
        if num > mid:
            lower += mid
        else:
            upper -= mid
        mid = (upper-lower)//2
    return True

def test():
    mx = float('-inf')
    for i in range(1, 10001):
        mx = max(mx, binary_search(i, [x for x in range(1, 10001)]))
    return mx

print(test())
