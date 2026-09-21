class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        if len(piles) == h:
            return max(piles)

        def tryK(k):
            count = 0
            for i in range(len(piles)):
                count += (piles[i] // k)
                if ((piles[i] % k) != 0):
                    count += 1

            return count

        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = tryK(mid)
            if hours > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1

        return res





