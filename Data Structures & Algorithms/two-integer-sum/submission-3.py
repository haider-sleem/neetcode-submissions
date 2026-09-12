class Solution:
    def twoSum(self, arr: list[int], target: int) -> list[int]:
        """Finds the indices of two numbers in an array that add up to a target value.

        Args:
            arr (list[int]): The list of integers to search through.
            target (int): The target sum we want to achieve.

        Returns:
            list[int]: A list containing the two indices whose values add up 
            to the target, with the smaller index positioned first.
        """
        # Dictionary to store numbers we've seen so far as keys and their indices as values
        seen_dict = {}

        for i, n in enumerate(arr):
            # Calculate the required complement to reach the target sum
            needed_n = target - n

            # Check if we have already encountered the complement number in previous iterations
            if needed_n in seen_dict:
                # Return the smaller index first (from the dictionary) followed by the current index
                return [seen_dict[needed_n], i]

            # Store the current number and its index for future lookups
            seen_dict[n] = i