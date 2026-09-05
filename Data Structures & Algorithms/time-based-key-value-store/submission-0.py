class TimeMap:
    """A time-based key-value data structure that stores multiple values

    for the same key at different timestamps.
    """

    def __init__(self):
        """Initializes the TimeMap object with an empty storage dictionary."""
        # Maps key (str) to a list of [timestamp, value] pairs
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        """Stores the key with the value at the given timestamp.

        Args:
            key: The string key identifier.
            value: The string value to associated with the key.
            timestamp: The integer timestamp for the entry.
        """
        if key not in self.store:
            self.store[key] = []

        # Timestamps are strictly increasing, so the list remains sorted
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        """Retrieves the value associated with key at or before given timestamp.

        Args:
            key: The string key identifier to look up.
            timestamp: The target timestamp integer.

        Returns:
            The value string with the largest timestamp <= target timestamp.
            Returns an empty string if no such value exists.
        """
        if key not in self.store:
            return ""

        values = self.store[key]
        res = ""

        # Binary search pointers based on array indices
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            # Exact timestamp match found
            if values[mid][0] == timestamp:
                return values[mid][1]

            # Current timestamp is valid; save candidate and search right for a closer one
            elif values[mid][0] < timestamp:
                res = values[mid][1]
                left = mid + 1

            # Current timestamp is too large; search left
            else:
                right = mid - 1

        return res