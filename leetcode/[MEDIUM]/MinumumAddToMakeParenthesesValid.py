class Solution:
    def minAddToMakeValid(self, S):
        stack = list()
        
        for s in S:
            if not stack:
                stack.append(s)
            else:
                if s == ')' and stack[-1] == '(':
                    stack.pop(-1)
                else:
                    stack.append(s)
        return len(stack)