class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(list(set(nums)))
        print(nums)
        return sorted(set(nums)) != sorted(nums)