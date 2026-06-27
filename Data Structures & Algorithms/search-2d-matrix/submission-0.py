class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        high = (m * n) - 1
        low = 0
        while low <= high:
            mid = low + (high - low) // 2
            mid_value = matrix[mid // n][mid % n]
            if target == mid_value:
                return True
            elif target > mid_value:
                low = mid + 1
            else:
                high = mid - 1
        return False