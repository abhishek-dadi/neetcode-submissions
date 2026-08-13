class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Step 1: Sort the array
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Optimization: If the smallest number is > 0, no 3 numbers can sum to 0
            if nums[i] > 0:
                break
                
            # Skip duplicates for the fixed first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Step 2: Set up Two Pointers for the remaining array
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for 'left' pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicate values for 'right' pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1   # Need a larger sum
                else:
                    right -= 1  # Need a smaller sum
                    
        return res