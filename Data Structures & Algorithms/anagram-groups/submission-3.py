class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        o1 = {}
        for s in strs:
            st= tuple(sorted(s))
            if st not in o1: o1[st] = []
            o1[st].append(s)
        return list(o1.values())