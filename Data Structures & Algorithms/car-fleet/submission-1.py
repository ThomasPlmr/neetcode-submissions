class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        map = dict()
        for i in range(n):
            map[position[i]] = (target-position[i])/speed[i]

        # {position:time left}

        stack = []
        temp = position
        temp.sort()
        position = temp[::-1] #now in largest to smallest order

        for i in range(n):
            if stack:
                if not (map[position[i]] <= map[stack[-1]]):
                    stack.append(position[i])
            else:
                stack.append(position[i])

        return len(stack)





