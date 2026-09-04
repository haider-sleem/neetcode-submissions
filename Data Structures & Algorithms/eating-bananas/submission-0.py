class Solution:

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """Finds the minimum integer eating speed k to finish all bananas within h hours.

        Args:
            piles: A list of integers where each element is the number of bananas in a pile.
            h: The maximum number of hours available to eat all bananas.

        Returns:
            The minimum integer rate k (bananas per hour).

        Complexity:
            Time: O(n log m), where n is len(piles) and m is max(piles).
            Space: O(1), using only scalar variables.
        """
        low = 1
        high = max(piles)
        result = high

        while low <= high:
            # Test candidate speed k (middle point)
            k = (low + high) // 2

            consumed_hours = 0
            for pile in piles:
                # Formula to round up integer division: ceil(pile / k)
                consumed_hours += (pile + k - 1) // k

            if consumed_hours <= h:
                # Save k as a valid solution candidate
                result = k
                # Try to find a smaller valid speed on the left side
                high = k - 1
            else:
                low = k + 1

        return result