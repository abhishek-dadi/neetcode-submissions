class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        left_count=1
        for i in range(n):
            res[i]=left_count
            left_count*=nums[i]
        right_count=1
        for i in range(n-1,-1,-1):
            res[i]*=right_count
            right_count*=nums[i]
        return res
        