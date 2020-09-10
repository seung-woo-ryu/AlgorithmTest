import copy

def solution(stones, k):
    start = min(stones)
    end = max(stones)
    n = len(stones)
    while start <= end:
        mid = (start + end)//2
        check = False
        tmp = 0
        for stone in stones:
            if stone - mid <= 0:
                tmp += 1
            else:
                tmp = 0
            if tmp >= k:
                check =True
                break
        if check:
            end = mid - 1
        else:
            start = mid + 1
    return mid