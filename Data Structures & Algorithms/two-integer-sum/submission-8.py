class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mydict:
                return [mydict[diff], i]
            mydict[nums[i]] = i
        