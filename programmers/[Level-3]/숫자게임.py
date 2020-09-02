def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    i,j = 0, 0
    while i < len(A):
        if A[i] < B[j]:
            i += 1
            j += 1
        else:
            i += 1
    return j