l = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

l1 = []
l2 = []

max_last = l[0]
diff = []

for x in range(len(l)):
    x1 = x

    max_curr = l[x1]

    if max_curr > max_last:
        max_last = max_curr
        diff.append(0)
    else:
        diff.append(max_last - l[x])


max_last2 = l[-1]
diff2 = []
for x in range(len(l) - 1, -1, -1):
    x1 = x

    max_curr = l[x1]

    if max_curr >= max_last2:
        max_last2 = max_curr
        diff2.insert(0, 0)
    else:
        diff2.insert(0, max_last2 - l[x])

c = 0

for i1, i2 in zip(diff, diff2):
    c += min(i1, i2)
