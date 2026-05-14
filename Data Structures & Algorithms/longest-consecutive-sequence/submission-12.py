class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(list(set(nums)))

        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1

        current_longest_seq = 1
        max_longest_seq = 0

        for index in range(len(nums) - 1):
            if nums[index] + 1 == nums[index+1]:
                current_longest_seq += 1
            else:
                current_longest_seq = 1
            
            if max_longest_seq <= current_longest_seq:
                max_longest_seq = current_longest_seq
        
        return max_longest_seq