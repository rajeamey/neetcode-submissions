class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = []
        for i in range(len(temperatures)):
            stack = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    stack += 1
                    final.append(stack)
                    break
                else:
                    stack += 1
            else:
                final.append(0)
        
        return final