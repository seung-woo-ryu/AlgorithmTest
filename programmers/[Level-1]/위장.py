'''
    EX)
    A주머니: N
    B주머니: M
    C주머니: K
    일 때 나올 수 있는 모든 조합의 갯수는
    없는 걸 가능하다 쳤다면
    (N+1)*(M+1)*(k+1)이다.
'''

def solution(clothes):
    di = dict()
    for c in clothes:
        if c[1] in di:
            di[c[1]] += 1
        else:
            di[c[1]] = 1
                
    cnt = 1
    for x in di.values():
        cnt *= x+1
    return cnt - 1
