class Solution:
    """
    Problem: Given an array nums, return an array answer such that answer[i] 
    is equal to the product of all elements of nums except nums[i].
    
    Constraints:
    - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer
    - Must solve in O(n) time and without using division
    
    Example:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]
    Explanation: 
    - For index 0: 2 * 3 * 4 = 24
    - For index 1: 1 * 3 * 4 = 12
    - For index 2: 1 * 2 * 4 = 8
    - For index 3: 1 * 2 * 3 = 6
    """
    
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Calculate product of all elements except self using two passes approach.
        
        Args:
            nums (list[int]): Input array of integers
            
        Returns:
            list[int]: Array where each element is product of all numbers except self
            
        Time Complexity: O(n) - two passes through the array
        Space Complexity: O(1) - excluding the output array
        """
        n = len(nums)
        result = [1] * n  # Initialize result array with 1s
        left_product = 1  # Running product of elements to the left
        right_product = 1 # Running product of elements to the right

        # First pass: Calculate products of all elements to the left
        # At each index i, result[i] will contain product of all numbers to its left
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        # Second pass: Multiply each element by products of all elements to the right
        # Going backwards, multiply each result[i] with product of all numbers to its right
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]

        return result


# Test cases
product_except_self = Solution()
print(product_except_self.productExceptSelf([1,2,3,4]))  # Expected: [24,12,8,6]
print(product_except_self.productExceptSelf([-1,1,0,-3,3]))  # Expected: [0,0,9,0,0]