import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = self.cleanS(s)
        return s == s[::-1]
    
    def cleanS(self, s: str) -> str:
        return re.sub(r'[^a-zA-Z0-9]', '', s)
