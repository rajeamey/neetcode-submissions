class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            if heights[left] <= heights[right]:
                area = heights[left] * (right - left)
            elif heights[left] > heights[right]:
                area = heights[right] * (right - left)
        
            if area > max_area:
                max_area = area

            right -= 1
            if left == right:
                left += 1
                right = len(heights) - 1

        return max_area