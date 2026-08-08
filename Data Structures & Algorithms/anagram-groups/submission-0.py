class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for s in strs:
            code = [0] * 26
            for c in s:
                code[ord(c) - ord('a')] += 1
            mydict[tuple(code)].append(s)   #tuple converts [] to (), now we can add to mydict
        return list(mydict.values())
