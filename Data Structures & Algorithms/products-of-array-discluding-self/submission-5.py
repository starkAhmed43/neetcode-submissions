class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        right_prod = left_prod.copy()
        left_prod[0] = nums[0]
        right_prod[-1] = nums[-1]
        
        # L -> R
        for i in range(1,len(nums)):
            left_prod[i] = left_prod[i-1] * nums[i]
        
        # R -> L
        for i in range(-2, -1*len(nums)-1, -1):
            right_prod[i] = right_prod[i+1] * nums[i]

        # print(left_prod)
        # print(right_prod)

        prods = [0] * len(nums)
        prods[0] = right_prod[1]
        prods[-1] = left_prod[-2]
        for i in range(1, len(nums)-1):
            prods[i] = left_prod[i-1] * right_prod[i+1]
        return prods