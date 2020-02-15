import sys

sys.setrecursionlimit(15000)


class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        array = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        xd = ''
        lcs = ''

        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    array[i + 1][j + 1] = array[i][j] + 1
                else:
                    array[i + 1][j + 1] = max(array[i][j + 1], array[i + 1][j])

        n = len(str1)
        m = len(str2)
        while array[n][m] != 0:

            if array[n][m] == array[n - 1][m]:
                xd = str1[n - 1] + xd
                n -= 1
            elif array[n][m] == array[n][m - 1]:
                xd = str2[m - 1] + xd
                m -= 1
            else:
                xd = str1[n - 1] + xd
                lcs = str1[n - 1] + lcs
                n -= 1
                m -= 1

        xd = str1[:n] + xd
        xd = str2[:m] + xd

        return xd


# str1 = "a"
# str2 = "b"
# print(Solution().shortestCommonSupersequence(str1, str2), 'ab')
# print()
# #
# str1 = "ad"
# str2 = "ab"
# print(Solution().shortestCommonSupersequence(str1, str2), 'adb')
# print()

str1 = "abcc"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2), 'cabcc')
print()
#
# str1 = "abc"
# str2 = "ab"
# print(Solution().shortestCommonSupersequence(str1, str2), 'abc')
# print()
#
# str1 = "abcd"
# str2 = "gbhd"
# print(Solution().shortestCommonSupersequence(str1, str2), 'agbchd')
# print()
#
# str1 = "bbbaaaba"
# str2 = "bbababbb"
# asda = 'bbababbaaba'
# asss = "bbabaaababb"
# ans = Solution().shortestCommonSupersequence(str1, str2)
# print(ans, ans == "bbabaaababb", len(ans), len('bbabaaababb'))
# print(ans)
# print('bbabaaababb')
# print()
#
# str1 = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdas"
# str2 = "qweqweqweqweqweqweqweqweqweqweqweqweqweqweqw"
# print(Solution().shortestCommonSupersequence(str1, str2), 'cabac')
# print()
#
str1 = "bcacaaab"
str2 = "bbabaccc"
ans = Solution().shortestCommonSupersequence(str1, str2)
print(ans, "bbabacacaaabc")
print(ans, ans == "bbabacacaaabc", len(ans), len('bbabacacaaabc'))
print()
#
# str1 = "atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllqmvptwammerobtgmkpowndejvbuwbporfyroknrjoekdgqqlgzxiisweeegxajqlradgcciavbpgqjzwtdetmtallzyukdztoxysggrqkliixnagwzmassthjecvfzmyonglocmvjnxkcwqqvgrzpsswnigjthtkuawirecfuzrbifgwolpnhcapzxwmfhvpfmqapdxgmddsdlhteugqoyepbztspgojbrmpjmwmhnldunskpvwprzrudbmtwdvgyghgprqcdgqjjbyfsujnnssfqvjhnvcotynidziswpzhkdszbblustoxwtlhkowpatbypvkmajumsxqqunlxxvfezayrolwezfzfyzmmneepwshpemynwzyunsxgjflnqmfghsvwpknqhclhrlmnrljwabwpxomwhuhffpfinhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdipldofyvfdurbsoxdurlofkqnrjomszjimrxbqzyazakkizojwkuzcacnbdifesoiesmkbyffcxhqgqyhwyubtsrqarqagogrnaxuzyggknksrfdrmnoxrctntngdxxechxrsbyhtlbmzgmcqopyixdomhnmvnsafphpkdgndcscbwyhueytaeodlhlzczmpqqmnilliydwtxtpedbncvsqauopbvygqdtcwehffagxmyoalogetacehnbfxlqhklvxfzmrjqofaesvuzfczeuqegwpcmahhpzodsmpvrvkzxxtsdsxwixiraphjlqawxinlwfspdlscdswtgjpoiixbvmpzilxrnpdvigpccnngxmlzoentslzyjjpkxemyiemoluhqifyonbnizcjrlmuylezdkkztcphlmwhnkdguhelqzjgvjtrzofmtpuhifoqnokonhqtzxmimp"
# str2 = "xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhfafiervrsyuiseumzmymtvsdsowmovagekhevyqhifwevpepgmyhnagjtsciaecswebcuvxoavfgejqrxuvnhvkmolclecqsnsrjmxyokbkesaugbydfsupuqanetgunlqmundxvduqmzidatemaqmzzzfjpgmhyoktbdgpgbmjkhmfjtsxjqbfspedhzrxavhngtnuykpapwluameeqlutkyzyeffmqdsjyklmrxtioawcrvmsthbebdqqrpphncthosljfaeidboyekxezqtzlizqcvvxehrcskstshupglzgmbretpyehtavxegmbtznhpbczdjlzibnouxlxkeiedzoohoxhnhzqqaxdwetyudhyqvdhrggrszqeqkqqnunxqyyagyoptfkolieayokryidtctemtesuhbzczzvhlbbhnufjjocporuzuevofbuevuxhgexmckifntngaohfwqdakyobcooubdvypxjjxeugzdmapyamuwqtnqspsznyszhwqdqjxsmhdlkwkvlkdbjngvdmhvbllqqlcemkqxxdlldcfthjdqkyjrrjqqqpnmmelrwhtyugieuppqqtwychtpjmloxsckhzyitomjzypisxzztdwxhddvtvpleqdwamfnhhkszsfgfcdvakyqmmusdvihobdktesudmgmuaoovskvcapucntotdqxkrovzrtrrfvoczkfexwxujizcfiqflpbuuoyfuoovypstrtrxjuuecpjimbutnvqtiqvesaxrvzyxcwslttrgknbdcvvtkfqfzwudspeposxrfkkeqmdvlpazzjnywxjyaquirqpinaennweuobqvxnomuejansapnsrqivcateqngychblywxtdwntancarldwnloqyywrxrganyehkglbdeyshpodpmdchbcc"
# print(Solution().shortestCommonSupersequence(str1, str2), 'cabac')
# print()
