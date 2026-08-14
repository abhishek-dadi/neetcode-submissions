class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # int(a / b) truncates towards zero (unlike a // b)
                stack.append(int(a / b))
            else:
                # Any non-operator string is guaranteed to be a valid integer
                stack.append(int(token))
                
        return stack[0]