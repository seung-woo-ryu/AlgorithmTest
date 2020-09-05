def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    cnt = 0
    for i in range(len(A)):
        if A[i] < B[cnt]:
            cnt += 1
    return cnt