def solution(s):
    stack = []
    
    for x in s:
        if len(stack) == 0:
            stack.append(x)
        elif stack[-1] == x:
            stack.pop()
        else:
            stack.append(x)
    return 1 if not len(stack) else 0