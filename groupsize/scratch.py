import collections

groupSizes = [3,3,3,3,3,1,3]
output = []

# hasz_map = {}

# for i, x in enumerate(groupSizes):
#     if x not in hasz_map:
#         hasz_map[x] = [i]
#     else:
#         hasz_map[x].append(i)
#
#     if len(hasz_map[x]) == x:
#         output.append(hasz_map[x])
#         hasz_map[x] = []
#

count = collections.defaultdict(list)
for i, size in enumerate(groupSizes):
    count[size].append(i)

for i, x in count.items():
    for elem in x:
        elem



print(output)