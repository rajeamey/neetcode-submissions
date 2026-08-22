class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for st in strs:
            count = [0] * 26

            for c in st:
                count[ord(c) - ord('a')] += 1
            
            if tuple(count) in res:
                res[tuple(count)].append(st)
            else:
                res[tuple(count)] = [st]
        
        return list(res.values())