class Solution:

  def findMedianSortedArrays(
      self, nums1: list[int], nums2: list[int]
  ) -> float:
    """Finds the median of two sorted arrays in O(log(min(n, m))) time.

    Uses binary search on the smaller array to partition both arrays into two
    halves, ensuring all elements in the left partition are less than or equal
    to all elements in the right partition.

    Args:
        nums1: A sorted list of integers.
        nums2: A sorted list of integers.

    Returns:
        The median of the combined sorted arrays as a float.

    Time Complexity:
        O(log(min(n, m))) where n and m are the lengths of nums1 and nums2.

    Space Complexity:
        O(1) auxiliary space.
    """
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    # Ensure A is always the smaller array
    if len(A) > len(B):
      A, B = B, A

    l, r = 0, len(A) - 1

    while True:
      i = (l + r) // 2  # Partition index for A
      j = half - i - 2  # Partition index for B

      # Handle boundary values near the partition line
      A_left = A[i] if i >= 0 else float("-inf")
      A_right = A[i + 1] if (i + 1) < len(A) else float("inf")
      B_left = B[j] if j >= 0 else float("-inf")
      B_right = B[j + 1] if (j + 1) < len(B) else float("inf")

      # Check if the partition is correct
      if A_left <= B_right and B_left <= A_right:
        # Odd total length
        if total % 2 != 0:
          return min(A_right, B_right)
        # Even total length
        return (max(A_left, B_left) + min(A_right, B_right)) / 2

      # Adjust binary search pointers
      elif A_left > B_right:
        r = i - 1  # Too many elements taken from A
      else:
        l = i + 1  # Too few elements taken from A