class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remaining = target - nums[i]
            remaining_indices = list(range(len(nums)))
            remaining_indices.pop(i)
            for j in remaining_indices:
                if nums[j] == remaining:
                    return sorted([i,j])
        