class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data_dict = {}
        for num in nums:
            if num in data_dict:
                data_dict[num] += 1
            else:
                data_dict[num] = 1
        
        data_dict = dict(sorted(data_dict.items(), key=lambda item: item[1], reverse=True))
        return list(data_dict.keys())[:k]