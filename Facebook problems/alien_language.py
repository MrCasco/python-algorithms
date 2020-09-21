def alien_language(words, code):
    valid = lambda x, y: code.index(x) <= code.index(y)
    i = 0
    w1 = words[0]
    w2 = words[1]
    low = min(len(w1), len(w2))
    if valid(w1[i], w2[i]) and w1[0] != w2[0]:
        return True
    elif not valid(w1[i], w2[i]):
        return False
    else:
        while True:
            if i >= low:
                if len(w1) == low:
                    return True
                else:
                    return False
            if w1[i] == w2[i]:
                i += 1
            else:
                return valid(w1[i], w2[i])

print(alien_language(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'))
print(alien_language(['apple', 'app'], 'abcdefghijlkmnopqrstuvwxyz'))
