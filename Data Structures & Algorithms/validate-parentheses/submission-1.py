class Solution:
    def isValid(self, s: str) -> bool:
        mapping={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i in mapping:
                t=stack.pop() if stack else '#'
                if mapping[i]!=t:
                    return False
            else:
                stack.append(i)
        return not stack                
        