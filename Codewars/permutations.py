def permutations(word):
    calculate(word, 0, len(word)-1)

def calculate(word, left, right):
    if left == right:
        print(word)
    else:
        for i in range(left, right+1):
            temp = swap(word, left, i)
            calculate(temp, left+1, right)

def swap(w, x, y):
    lst = list(w)
    lst[x], lst[y] = lst[y], lst[x]
    return ''.join(lst)

print(permutations('1234'))
