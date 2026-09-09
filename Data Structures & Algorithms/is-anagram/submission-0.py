class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Determines if two strings are anagrams of each other using sorting."""
        return sorted(s) == sorted(t)