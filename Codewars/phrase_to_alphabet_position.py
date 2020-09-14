def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetCaps = alphabet.upper()
    code = dict(zip(alphabet[::1], [i+1 for i in range(26)]))
    res = ''
    for letter in text:
        if letter in alphabet or letter in alphabetCaps:
            res += str(code[letter.lower()])
        else:
            continue
        res += ' '
    return res[:-1]

if alphabet_position("The narwhal bacons at midnight.") == '20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20':
    print('correct')
else:
    print('not')
