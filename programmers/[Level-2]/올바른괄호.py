def solution(s):
    n = 0
    for x in s:
        n += 1 if x =='(' else -1
        if n <0:
            return False
    if n == 0:
        return True
    else:
        return False
