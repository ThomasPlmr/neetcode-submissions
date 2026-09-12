class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        '''
        Input: temperatures = [30,38,30,36,35,40,28]

        Output: [1,4,1,2,1,0,0]
        '''
        temp = temperatures
        n = len(temp)
        output = [0] * n
        stack = []

        for i in range(n-1, -1, -1):

            # Pop all cooler temperatures
            while stack and temp[i] >= temp[stack[-1]]:
                stack.pop()
            
            # Record answer
            if stack:
                output[i] = stack[-1] - i
            
            # Push current index
            stack.append(i)

        return output














