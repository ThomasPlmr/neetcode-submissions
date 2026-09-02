class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])

        stck = []

        for vals in tokens:
            if (vals == "+"):
                output = (stck[-1] + stck[-2])
                stck.pop()
                stck.pop()
                stck.append(output)
            elif (vals == "-"):
                output = (stck[-2] - stck[-1])
                stck.pop()
                stck.pop()
                stck.append(output)
            elif (vals == "*"):
                output = (stck[-2] * stck[-1])
                stck.pop()
                stck.pop()
                stck.append(output)
            elif (vals == "/"):
                output = int(stck[-2] / stck[-1])
                stck.pop()
                stck.pop()
                stck.append(output)
            else:
                stck.append(int(vals))

        return stck[0]








