import math

def solution(n, stations, w):
    answer = 0
    start = 0
    for station in stations:
        L = station - w
        length = L - start - 1
        if length > 0:
            answer += math.ceil( length / ( 2 * w + 1 ))
        start = station + w
    
    if start < n:
        answer += math.ceil(( n - start ) / (2 * w + 1))
    return answer