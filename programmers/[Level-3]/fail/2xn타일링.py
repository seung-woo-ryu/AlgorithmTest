def solution(n):
    n1 = 1
    n2 = 1
    for _ in range(2,n+1):
        n1,n2 = n2, n1+ n2
        
    return n2 % 1000000007