def get_pins(observed):
    keys = {
        '1':['1','2','4'],
        '2':['2','1','3','5'],
        '3':['2','3','6'],
        '4':['4','1','5','7'],
        '5':['2','4','5','6','8'],
        '6':['3','5','6','9'],
        '7':['4','7','8'],
        '8':['8','5','7','9','0'],
        '9':['6','8','9'],
        '0':['0','8']
    }
    i = 0
    base = keys[observed[0]]
    while i < len(observed)-1:
        curr_sol = []
        import ipdb; ipdb.set_trace()
        for letter in keys[observed[i+1]]:
            for comb in base:
                curr_sol.append(comb + letter)
        i += 1
        base = curr_sol
    return base
