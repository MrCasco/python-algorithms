"""
You are given an array(list) strarr of strings and an integer k.
Your task is to return the first longest string consisting of k consecutive strings taken in the array.

For example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
"""

def longest_consec(strarr, k):
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ''

    #NAIVE SOLUTION
    ln = 0
    mx = 0
    consec = ''
    res = ''
    for i in range(len(strarr)-k+1):
      for word in strarr[i:i+k]:
          consec += word
          ln  = len(consec)
      if ln > mx:
          mx = ln
          res = consec
      consec = ''
    return res

    # COMPACT SOLUTION
    # mx = 0
    # consec = ''
    # res = ''
    # for i in range(len(strarr)-k+1):
    #     consec = strarr[i:i+k]
    #     if len(''.join(word for word in consec)) > mx:
    #         mx = len(''.join(word for word in consec))
    #         res = consec
    #     consec = ''
    # return ''.join(a for a in res)

def test(testing, answer):
    if testing != answer:
        print('wrong ' + testing)
    else:
        print(answer + ' is ok')


test(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
test(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1), "oocccffuucccjjjkkkjyyyeehh")
test(longest_consec([], 3), "")
test(longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2), "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck")
test(longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2), "wlwsasphmxxowiaxujylentrklctozmymu")
test(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
test(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
test(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
test(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")
