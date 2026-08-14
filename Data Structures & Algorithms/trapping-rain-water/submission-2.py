class Solution:
    def trap(self, height: List[int]) -> int:
        #remove 0 from edges
        temp = 0
        for j in range(len(height)):
            if height[j] != 0:
                temp = j
                break
        if (temp != 0):
            height = height[temp:]

        temp = 0
        reverse = height[::-1]
        for j in range(len(reverse)):
            if reverse[j] != 0:
                temp = j
                break
        if (temp != 0):
            reverse = reverse[temp:]

        height = reverse[::-1]
        #works
        #maxL and maxR for each now!
        # for better memory we could go backwards rather than inverting the array
        maxL = []
        c_max = 0
        for i in range(len(height)):
            maxL.append(c_max)
            c_max = max(c_max, height[i])

        maxR = []
        c_max = 0
        rheight = height[::-1]
        for i in range(len(rheight)):
            maxR.append(c_max)
            c_max = max(c_max, rheight[i])
        maxR = maxR[::-1]
        #maxL and maxR done
        minBoth = []
        for i in range(len(maxL)):
            minBoth.append(min(maxL[i], maxR[i]))

        #min both done
        water = 0
        for i in range(len(minBoth)):
            temp = minBoth[i] - height[i]
            if temp > 0:
                water += temp

        return water
        




