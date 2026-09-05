class Solution:

    def search(self, nums: list[int], target: int) -> int:
        """Searches for a target value in a rotated sorted array using binary search.

        Args:
            nums: A list of unique integers sorted in ascending order and rotated
              between 1 and n times.
            target: The integer value to search for within the array.

        Returns:
            The zero-based index of target if found in nums; otherwise -1.

        Complexity:
            Time: O(log n), where n is the length of nums, as the search space
              is halved in each iteration.
            Space: O(1), as the search is performed in-place using constant extra
              memory.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Found target
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1