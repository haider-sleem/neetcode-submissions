class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setnums = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [min(i, j), max(i, j)]
            
