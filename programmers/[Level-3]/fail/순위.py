def solution(n, results):
    win = {}
    lose = {}
    
    for i in range(1,n+1):
        win[i] = set()
        lose[i] = set()
        
    for i in range(1,n+1):
        for r in results:
            if r[0] == i:
                win[i].add(r[1])
            if r[1] == i:
                lose[i].add(r[0])
        for L in win[i]:
            lose[L].update(lose[i])
        for W in lose[i]:
            win[W].update(win[i])
    answer = 0
    for i in range(1,n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer +=1
    return answer