# strs = ["011","1","11","0","010","1","10","1","1","0","0","0","01111","011","11","00","11","10","1","0","0","0","0","101","001110","1","0","1","0","0","10","00100","0","10","1","1","1","011","11","11","10","10","0000","01","1","10","0"]
# m = 44 # 0
# n = 39 # 1

# strs = ['1000', '111', '1000', '1000']
# m = 9 # 0
# n = 3 # 1

# strs = ['1', '10', '0']
# m = 1 # 0
# n = 2 # 1

strs = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101", "0", "11", "01",
        "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"]
m = 9
n = 80

memo = {}


def find_max(strs, i, zeros_num, ones_num, memo):
    output = 0
    if (i, zeros_num, ones_num) in memo:
        return memo[(i, zeros_num, ones_num)]

    if i < len(strs):
        if zeros_num > 0 or ones_num > 0:
            mc, nc = strs[i].count('0'), strs[i].count('1')

            take = 0

            skip = find_max(strs, i + 1, zeros_num, ones_num, memo)

            if mc <= zeros_num and nc <= ones_num:
                take = find_max(strs, i + 1, zeros_num - mc, ones_num - nc, memo) + 1

            output = max(take, skip)

    memo[(i, zeros_num, ones_num)] = output
    return output


output = find_max(strs, 0, m, n, memo)
