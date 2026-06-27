class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            # check if left sorted
            if nums[mid] < nums[high]:
                high = mid
            # check if right sorted 
            else:
                low = mid + 1
            
        
        return nums[low]