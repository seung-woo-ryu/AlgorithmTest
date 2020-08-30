from itertools import combinations

def solution(nums):
    answer = 0
    n=50000
    a = [False,False] + [True]*(n-1)
    primes=[]
    
    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                 a[j] = False
    
    for li in list(combinations(nums,3)):
        if a[li[0] + li[1] + li[2]]:
            answer +=1

    return answer
