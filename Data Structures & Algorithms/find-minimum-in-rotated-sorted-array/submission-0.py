class Solution:

    def findMin(self, nums: list[int]) -> int:
        """Finds the minimum element in a rotated sorted array using binary search.

        Args:
            piles: A list of unique integers rotated between 1 and n times.

        Returns:
            The minimum integer in the array.

        Complexity:
            Time: O(log n), where n is the length of nums.
            Space: O(1), using constant extra memory.
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid is greater than right, minimum is in the right unsorted part
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, minimum is in the left part or at mid itself
            else:
                right = mid

        # Loop ends when left == right, pointing directly to the smallest element
        return nums[left]