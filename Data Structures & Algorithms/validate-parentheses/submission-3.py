class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        parenthesis_map = {
            "[": "]",
            "(": ")",
            "{": "}"
        }
        stack = []
    
        for el in s:
            if el in parenthesis_map:
                stack.append(parenthesis_map[el])
            else:
                if not stack:
                    return False

                stack_top = stack.pop()
                if el != stack_top:
                    return False
        if stack:
            return False

        return True