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
        n = 0
        str1_loc = 0
        str2_loc = 0

        for i in range(len(str1)):
            for j in range(len(str2)):

                if str1[i] == str2[j]:
                    array[i + 1][j + 1] = array[i][j] + 1

                    if array[i + 1][j + 1] > n:
                        n += 1
                        xd += str1[str1_loc:i]
                        xd += str2[str2_loc:j]
                        xd += str1[i]
                        lcs += str1[i]

                        str1_loc = i + 1
                        str2_loc = j + 1
                        a= 1

                else:
                    array[i + 1][j + 1] = max(array[i][j + 1], array[i + 1][j])

        xd += str1[str1_loc:]
        xd += str2[str2_loc:]
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
#
# str1 = "abcc"
# str2 = "cab"
# print(Solution().shortestCommonSupersequence(str1, str2), 'cabcc')
# print()
# #
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

str1 = "bcacaaab"
str2 = "bbabaccc"
print(Solution().shortestCommonSupersequence(str1, str2), "bbabacacaaabc")
print()

str1 = "atdznrqfwlfbcqkezrltzyeqvqemikzgghxkzenhtapwrmrovwtpzzsyiwongllqmvptwammerobtgmkpowndejvbuwbporfyroknrjoekdgqqlgzxiisweeegxajqlradgcciavbpgqjzwtdetmtallzyukdztoxysggrqkliixnagwzmassthjecvfzmyonglocmvjnxkcwqqvgrzpsswnigjthtkuawirecfuzrbifgwolpnhcapzxwmfhvpfmqapdxgmddsdlhteugqoyepbztspgojbrmpjmwmhnldunskpvwprzrudbmtwdvgyghgprqcdgqjjbyfsujnnssfqvjhnvcotynidziswpzhkdszbblustoxwtlhkowpatbypvkmajumsxqqunlxxvfezayrolwezfzfyzmmneepwshpemynwzyunsxgjflnqmfghsvwpknqhclhrlmnrljwabwpxomwhuhffpfinhnairblcayygghzqmotwrywqayvvgohmujneqlzurxcpnwdipldofyvfdurbsoxdurlofkqnrjomszjimrxbqzyazakkizojwkuzcacnbdifesoiesmkbyffcxhqgqyhwyubtsrqarqagogrnaxuzyggknksrfdrmnoxrctntngdxxechxrsbyhtlbmzgmcqopyixdomhnmvnsafphpkdgndcscbwyhueytaeodlhlzczmpqqmnilliydwtxtpedbncvsqauopbvygqdtcwehffagxmyoalogetacehnbfxlqhklvxfzmrjqofaesvuzfczeuqegwpcmahhpzodsmpvrvkzxxtsdsxwixiraphjlqawxinlwfspdlscdswtgjpoiixbvmpzilxrnpdvigpccnngxmlzoentslzyjjpkxemyiemoluhqifyonbnizcjrlmuylezdkkztcphlmwhnkdguhelqzjgvjtrzofmtpuhifoqnokonhqtzxmimp"
str2 = "xjtuwbmvsdeogmnzorndhmjoqnqjnhmfueifqwleggctttilmfokpgotfykyzdhfafiervrsyuiseumzmymtvsdsowmovagekhevyqhifwevpepgmyhnagjtsciaecswebcuvxoavfgejqrxuvnhvkmolclecqsnsrjmxyokbkesaugbydfsupuqanetgunlqmundxvduqmzidatemaqmzzzfjpgmhyoktbdgpgbmjkhmfjtsxjqbfspedhzrxavhngtnuykpapwluameeqlutkyzyeffmqdsjyklmrxtioawcrvmsthbebdqqrpphncthosljfaeidboyekxezqtzlizqcvvxehrcskstshupglzgmbretpyehtavxegmbtznhpbczdjlzibnouxlxkeiedzoohoxhnhzqqaxdwetyudhyqvdhrggrszqeqkqqnunxqyyagyoptfkolieayokryidtctemtesuhbzczzvhlbbhnufjjocporuzuevofbuevuxhgexmckifntngaohfwqdakyobcooubdvypxjjxeugzdmapyamuwqtnqspsznyszhwqdqjxsmhdlkwkvlkdbjngvdmhvbllqqlcemkqxxdlldcfthjdqkyjrrjqqqpnmmelrwhtyugieuppqqtwychtpjmloxsckhzyitomjzypisxzztdwxhddvtvpleqdwamfnhhkszsfgfcdvakyqmmusdvihobdktesudmgmuaoovskvcapucntotdqxkrovzrtrrfvoczkfexwxujizcfiqflpbuuoyfuoovypstrtrxjuuecpjimbutnvqtiqvesaxrvzyxcwslttrgknbdcvvtkfqfzwudspeposxrfkkeqmdvlpazzjnywxjyaquirqpinaennweuobqvxnomuejansapnsrqivcateqngychblywxtdwntancarldwnloqyywrxrganyehkglbdeyshpodpmdchbcc"
print(Solution().shortestCommonSupersequence(str1, str2), 'cabac')
print()
