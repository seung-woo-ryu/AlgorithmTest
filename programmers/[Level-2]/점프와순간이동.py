def solution(n):
    ans = 0
    
    while n:
        n, na = divmod(n,2)
        if na == 1:
            ans +=1

    return ans

solution(5000)