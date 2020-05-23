import random
def generateNationalID():
    fullid = '' 
    tmp = 0
    for i in reversed(range(2,14)):
        rnd = random.randint(1, 9)
        tmp += (i * rnd)
        fullid += str(rnd)
    tmp = tmp % 11
    if tmp == 0:
        tmp = 1
    elif tmp == 1:
        tmp = 0
    else:
        tmp = 11 - tmp
    fullid += str(abs(tmp))
    return fullid