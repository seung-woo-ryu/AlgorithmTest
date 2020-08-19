def solution(people, limit):
    people.sort()
    L = 0
    R = len(people) - 1
    answer = 0
    
    while L <= R:
        if R == L:
            answer  += 1
            return answer 
        if people[R] + people[L] <= limit:
            L += 1
            R -= 1
            answer += 1
        else:
            R -= 1
            answer += 1
            
    return answer