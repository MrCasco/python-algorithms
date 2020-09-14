input = int(input('input: '))
maxPow = 1
ones = 0

while(maxPow-input < 0):
    maxPow *= 2

while(maxPow%2 == 0):
    if(input-maxPow >= 0):
        maxPow = maxPow/2
        ones += 1

    elif(input-maxPow < 0):
        maxPow = maxPow/2

print(ones)
