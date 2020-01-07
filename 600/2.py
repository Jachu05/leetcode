from copy import copy

num = 31

bin_rep = bin(num)[2:]
zeros_rep = list('0' * len(bin_rep))
max_len = len(zeros_rep)


def min_nums(bin_rep, i, max_len, max_val):
    counter = 0

    if i < max_len:
        if int("".join(bin_rep), 2) <= max_val:
            counter = 1
        else:
            counter = 0
        skip_counter, use_counter = 0, 0
        print("".join(bin_rep), counter)

        bin_rep_c = copy(bin_rep)

        if 0 == i < max_len:
            bin_rep_c[i] = '1'
            bin_rep_c[i + 1] = '1'
            skip_counter = min_nums(bin_rep_c, i + 1, max_len, max_val)

            bin_rep_c[-1] = '1'
            use_counter = min_nums(bin_rep_c, i + 1, max_len, max_val)
        elif 0 < i <= max_len - 2:
            if i != max_len - 2 and bin_rep_c[-1] == '0':
                pass
            else:
                bin_rep_c[i] = '1'
                bin_rep_c[i + 1] = '1'

                bin_rep_c[i - 1] = '0'
                skip_counter = min_nums(bin_rep_c, i + 1, max_len, max_val)

                bin_rep_c[i - 1] = '1'
                use_counter = min_nums(bin_rep_c, i + 1, max_len, max_val)
        # elif i == max_len - 2 and bin_rep_c[i + 1] == '1':
        #     bin_rep_c[i] = '1'
        #     bin_rep_c[i - 1] = '0'
        #     skip_counter = min_nums(bin_rep_c, i + 1, max_len, max_val)
        #
        #     bin_rep_c[i - 1] = '1'
        #     use_counter = min_nums(bin_rep_c, i + 1, max_len, max_val)

        counter = counter + skip_counter + use_counter

    return counter


xd = min_nums(zeros_rep, 0, max_len, num)
output = num - (xd - 1)
