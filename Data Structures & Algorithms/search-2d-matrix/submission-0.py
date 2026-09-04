class Solution:
    """Provides methods for searching element positions in 2D grids."""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Searches for a target integer in an m x n matrix using 2D Binary Search.

        Treats the 2D matrix as a virtual 1D sorted array by mapping 1D indices
        to 2D row and column positions.

        Args:
            matrix: A 2D list of integers where each row is sorted.
            target: The integer value to search for.

        Returns:
            True if target exists within the matrix, False otherwise.

        Complexity:
            Time: O(log(m * n))
            Space: O(1)
        """
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        left_index = 0
        right_index = (num_rows * num_cols) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            # Map the 1D index back to 2D matrix row and column
            current_row = mid_index // num_cols
            current_col = mid_index % num_cols
            current_value = matrix[current_row][current_col]

            if current_value == target:
                return True

            if current_value > target:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1

        return False