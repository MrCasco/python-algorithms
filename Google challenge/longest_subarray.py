"""
Given an array: [5,3,1,2,3,4,2]
"""

def longest_subarray(lst):
    curdif = lst[0]-lst[1]
    mx = 2
    curmx = mx
    for num1, num2 in zip(lst[1:], lst[2:]):
        if num1-num2 == curdif:
            curmx += 1
        else:
            curmx = 2
            curdif = num1-num2
        mx = max(mx, curmx)
    return mx

print(longest_subarray([5,3,1,2,3,4,2]))
print(longest_subarray([5,3]))
print(longest_subarray([5,3,1,2,3,4,2]))
print(longest_subarray([1,1,1,1,1]))
