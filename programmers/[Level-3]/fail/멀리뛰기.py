def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def combi(a,b):
    n = fact(a)
    r = fact(b)
    nmr = fact(a-b)
    return n //(r*nmr)
        
def solution(n):
    li = [[]]
    arr = [1]
    
    for _ in range(1,n+1):
        for idx in range(len(li)):
            li[idx].append(1)
            if idx:
                if li[idx].count(2) >= li[idx].count(1):
                    arr[idx] = combi(li[idx].count(2)+1,li[idx].count(1))
                else:
                    arr[idx] = (arr[idx] // (li[idx].count(1) + 1 - li[idx].count(2))) * (li[idx].count(1)+1)         
        if sum(li[idx]) % 2 == 0:
            li.append([2] * (sum(li[idx])//2))
            arr.append(1)
                            
    return sum(arr)%1234567

print(solution(1000))