import math

def solution(distance, rocks, n):
    
    rocks.append(distance)
    rocks.sort()
    
    left,right = 1, distance

    while left<=right:
        mid = (left+right)//2
        pre = 0
        r = 0
        m = math.inf
        
        for rock in rocks:
            if rock - pre < mid:
                r += 1
            else:
                m = min(m,rock-pre)
                pre = rock
        if r > n:
            right = mid -1
        else:
            answer = m
            left = mid + 1
    return answer                