def solution(n, k):
    answer = []
    li = [ _+1 for _ in range(n)]
    
    def fac(n):
        if n == 1:
            return 1
        else:
            return n * fac(n-1)
    
    factorial = fac(n-1)
    
    for i in range(n-1,0,-1):
        mok, na = divmod(k,factorial)
        mok -= 1 if na == 0 else 0
        k -= mok * factorial
        answer.append(li[mok])
        
        del li[mok]
        
        factorial //= i
        
    return answer + li

print(solution(3,2))