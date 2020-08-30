def solution(routes):
    routes.sort()
    answer = 0
    greed = []
    for x in routes:
        if not greed:
            greed = x
            answer += 1
        elif greed[1] < x[0]:
            greed = x
            answer += 1
        else:
            greed[0] = x[0]
            greed[1] = x[1] if greed[1] > x[1] else greed[1]
    
    return answer