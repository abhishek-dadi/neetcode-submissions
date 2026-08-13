class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_a=set(nums)
        nums_len=len(nums)
        set_len=len(set_a)
        if nums_len == set_len:
            return False
        else:
            return True
        