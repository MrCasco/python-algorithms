def max_contiguous(lst):
    prev = lst[0]
    gmx = prev
    for num in lst[1:]:
        prev = max(prev+num, num)
        gmx = max(prev, gmx)
    return gmx

print(max_contiguous([-2, 1, -3, 4, -1, 2, 1]))
## SOLUTION ##
## https://backtobackswe.com/platform/content/max-contiguous-subarray-sum/solutions ##
