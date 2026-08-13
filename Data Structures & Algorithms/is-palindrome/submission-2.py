class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalnum():
                i=i.lower()
                res=res+i
        if res==res[::-1]:
            return True
        else:
            return False