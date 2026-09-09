class Solution:
    """A solution class for array-related algorithmic problems."""

    def hasDuplicate(self, nums: list[int]) -> bool:
        """Determines if any value appears more than once in an array.

        This method leverages a hash set to efficiently detect duplicate
        elements by comparing the original list size against the unique
        elements set size.

        Args:
            nums (list[int]): The input list of integers to check.

        Returns:
            bool: True if any value appears more than once, False otherwise.
        """
        # Convert the list to a set. Sets only store unique elements,
        # which automatically removes any duplicates (O(n) time complexity).
        set_nums = set(nums)

        # If the original list is larger than the set, it means
        # duplicates existed and were filtered out by the set.
        if len(nums) > len(set_nums):
            return True

        return False