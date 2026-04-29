class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if set(s) != set(t):
            return False

        cache: dict = {}
        for el in s:
            if el not in cache:
                cache[el] = 1
            else:
                cache[el] += 1
        
        cache2: dict = {}
        for el2 in t:
            if el2 not in cache2:
                cache2[el2] = 1
            else:
                cache2[el2] += 1
        
        sset = set(s)
        for el3 in sset:
            if cache[el3] != cache2[el3]:
                return False
        
        return True
