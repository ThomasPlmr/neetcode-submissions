class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        if (len(cost) > 2):
            for i in range(len(cost)-1, -1, -1):
                if (i <= len(cost)-3):
                    cost[i] = min(cost[i+1], cost[i+2]) + cost[i]
            return min(cost[0], cost[1])

        else:
            return min(cost)
