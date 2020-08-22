def bi(n):
    cnt = 0
    while 0 != n:
        n,na =  divmod(n,2)
        cnt += 1 if na == 1 else 0
    
    return cnt

def solution(n):
    cnt = bi(n)
    while True:
        n += 1 
        if cnt == bi(n):
            return n