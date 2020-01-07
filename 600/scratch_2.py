def findIntegers(num):
    x, y = 1, 2
    res = 0
    num += 1
    while num:
        if num & 1 and num & 2:
            res = 0
        res += x * (num & 1)
        num >>= 1
        x, y = y, x + y
    return res


xd = findIntegers(31)
a=1