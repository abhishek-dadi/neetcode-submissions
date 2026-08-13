from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l=[]
        coun=Counter(nums)
        sorted_coun = dict(sorted(coun.items(), key=lambda x: x[1]))
        for items,freq in sorted_coun.items():
            l.append(items)
        res=[]
        for i in range(k):
            res.append(l[len(l)-1-i])
        return res


        