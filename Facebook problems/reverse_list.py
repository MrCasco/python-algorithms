def reverse_words(arr):
    arr.reverse()
    arr.append(' ')
    spaces = arr.count(' ')
    right = arr.index(' ')
    left = 0
    temp = []
    tmp = []
    for i in range(spaces-1):
        #import ipdb; ipdb.set_trace()
        tmp = arr[left:right]
        tmp.reverse()
        temp.append(tmp)
        arr = arr[right:]
        arr.insert(left, temp)
        left = right+1
        right = arr.index(' ', right)
    return arr

print(reverse_words(list('happy he is')))
