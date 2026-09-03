class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target integer in a sorted array using Binary Search.
        
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 
            current_val = nums[mid]

            if current_val == target:
                return mid 
            elif current_val > target:
                right = mid - 1  
            else:
                left = mid + 1   
                
        return -1