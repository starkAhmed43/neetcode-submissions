class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return sorted(set(nums)) != sorted(nums)