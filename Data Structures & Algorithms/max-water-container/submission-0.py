class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        maxi=0
        temp=0
        while i<j:
            temp=min(heights[i],heights[j])*(j-i)
            maxi=max(maxi,temp)
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return maxi

        