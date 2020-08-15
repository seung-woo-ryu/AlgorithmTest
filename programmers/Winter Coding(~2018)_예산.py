def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for i in d:
        if budget >= i:
            budget = budget - i
            answer = answer +1
        else:
            break
    return answer