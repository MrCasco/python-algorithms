# BEST SOLUTION BY CODEWARS
def anagrams(word, words):
    return [item for item in words if sorted(item)==sorted(word)]

# MY SOLUTION
def anagrams(word, words):
    unique = set(word)
    res = []
    for wrd in words:
        if len(wrd) != len(word):
            continue
        res.append(wrd)
        for letter in unique:
            if word.count(letter) != wrd.count(letter):
                res.pop(-1)
                break
    return res
