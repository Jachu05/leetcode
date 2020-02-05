class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        cache = {}

        n_moves = pow(8, K)

        def rec_move(N, K, r, c):

            key = (K, r, c)

            if key in cache:
                return cache[key]

            out = 0

            if 0 <= r < N and 0 <= c < N:

                if K > 0:

                    out1 = rec_move(N, K - 1, r + 2, c + 1)
                    out2 = rec_move(N, K - 1, r + 2, c - 1)
                    out3 = rec_move(N, K - 1, r - 2, c + 1)
                    out4 = rec_move(N, K - 1, r - 2, c - 1)
                    out5 = rec_move(N, K - 1, r - 1, c - 2)
                    out6 = rec_move(N, K - 1, r + 1, c - 2)
                    out7 = rec_move(N, K - 1, r - 1, c + 2)
                    out8 = rec_move(N, K - 1, r + 1, c + 2)

                    out = out1 + out2 + out3 + out4 + out5 + out6 + out7 + out8

                    cache[key] = out
                else:
                    return 1

            return out

        out = rec_move(N, K, r, c)

        return out / n_moves


# N - chessboard dim
# K - moves
# r-th row knight starts at
# c-th column knight starts at
print("Probability that the knight remains on the board after it has stopped moving:",
      Solution().knightProbability(N=3, K=2, r=0, c=0))

print("Probability that the knight remains on the board after it has stopped moving:",
      Solution().knightProbability(N=3, K=1, r=0, c=0))