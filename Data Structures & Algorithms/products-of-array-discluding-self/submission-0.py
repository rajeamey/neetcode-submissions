import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_array = []
        for i in range(len(nums)):
            product = 1
            for index, num in enumerate(nums):
                if i != index:
                    product *= num
            product_array.append(product)

        return product_array
