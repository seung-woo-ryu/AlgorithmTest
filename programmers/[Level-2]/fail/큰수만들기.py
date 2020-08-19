def solution(number, k):
    stack = list()

    for index, num in enumerate(number):

        while len(stack) > 0 and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack += list(number[index:])
            return ''.join(stack)
        stack.append(num)    
    return ''.join(stack[:-k])

print(solution("1231234",	3))

