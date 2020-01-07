from math import ceil

n = 4

xd = []
a = n//2

if n % 2:

    for i in range(-a, 0):
        xd.append(i)

    for i in range(0, a + 1):
        xd.append(i)

else:

    for i in range(-a, 0):
        xd.append(i)

    for i in range(1, a + 1):
        xd.append(i)
