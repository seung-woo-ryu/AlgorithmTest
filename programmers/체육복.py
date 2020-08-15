def solution(n, lost, reserve):
    slost = set(lost) - set(reserve)
    sreserve = set(reserve) - set(lost)
    
    answer = n - len(slost)
    
    for x in slost:
        if (x - 1) in sreserve:
            if (x - 1) not in slost:
                answer = answer + 1
                sreserve.remove(x - 1)
            
        elif (x + 1) in sreserve:
            if (x + 1) not in slost:
                answer = answer + 1
                sreserve.remove(x + 1)
            
    return answer