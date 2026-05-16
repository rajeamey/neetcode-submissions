class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pairs = list()
        nums = sorted(nums)
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum == 0:
                    pairs.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        
        unique_pairs = []
        for pair in pairs:
            if pair not in unique_pairs:
                unique_pairs.append(pair)

        return unique_pairs