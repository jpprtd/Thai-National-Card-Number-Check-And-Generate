def checkNationalID(nid):
    nLength = len(nid)
    tmp = 0
    if not nLength == 13:
        return False
    nid = list(nid)
    for i in reversed(range(2, nLength + 1)):
        tmp += (i * int(nid[abs(i - 13)]))
    tmp = tmp % 11
    if tmp == 0:
        tmp = 1
    elif tmp == 1:
        tmp = 0
    else:
        tmp = 11 - tmp
    if abs(tmp) == int(nid[12]):
        return True
    else:
        return False
