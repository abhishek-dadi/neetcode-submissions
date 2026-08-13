class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sets=set(s)
        sett=set(t)
        if sett!=sets:
            return False
        else:
            if len(s)!=len(t):
                return False
            else:
                for i in sett:
                    count1,count2=0,0
                    for j in s:
                        if i==j:
                            count1+=1
                    for k in t:
                        if i==k:
                            count2+=1
                    if count1!=count2:
                        return False
        return True




        