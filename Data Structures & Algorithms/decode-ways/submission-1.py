class Solution:
    def numDecodings(self, s: str) -> int:
        next1, next2 = 1, 0  # next1 = dp[i+1], next2 = dp[i+2]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                cur = 0
            else:
                cur = next1

            if i + 1 < len(s) and (s[i] == "1" or
               s[i] == "2" and s[i + 1] in "0123456"):
                cur += next2

            next2 = next1
            next1 = cur

        return next1