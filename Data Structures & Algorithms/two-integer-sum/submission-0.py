class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            nt = target - num

            if nt in mp:
                return [mp[nt], i]

            mp[num] = i
