class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for i, j in count.items():
            freq[j].append(i)
        
        res = []
        for f in freq[::-1]:
            for s in f:
                res.append(s)
                if len(res) == k:
                    return res