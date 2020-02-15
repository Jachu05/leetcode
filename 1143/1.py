class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        :type text1: str
        :type text2: str
        :rtype: str
        """
        array = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    array[i + 1][j + 1] = array[i][j] + 1
                else:
                    array[i + 1][j + 1] = max(array[i][j + 1], array[i + 1][j])

        return array[-1][-1]
