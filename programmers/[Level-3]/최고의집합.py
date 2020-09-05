def solution(n, s):
    if s < n:
        return [-1]
    answer = []
    
    while n:
        mok = s//n
        answer.append(mok)
        s -= mok
        n -= 1

    return answer