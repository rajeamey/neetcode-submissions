class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index = 0
        index2 = 1
        max_index = len(nums) - 1
        while True:
            if nums[index] + nums[index2] == target:
                return [index, index2]

            if index2 != max_index:
                index2 += 1
            elif index != max_index - 1:
                index += 1
                index2 = index + 1
            else: break
        
        return []