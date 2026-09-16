class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []

        for i in range(len(matrix)-1, -1, -1):
            if (matrix[i][0] <= target):
                nums = matrix[i]
                break

        l = 0
        r = len(nums)-1

        while (l <= r):
            m = (l+r)//2

            if (nums[m] == target):
                return True
            elif (nums[m] < target):
                l = m + 1
            else:
                r = m - 1
        
        return False
