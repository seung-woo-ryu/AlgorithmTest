def solution(n, edge):
    queue = [1]
    visited =[-1,0] + [-1]* (n-1)
    
    arr = [[] for _ in range(n+1)]
    
    for e in edge:
        arr[e[0]].append(e[1])
        arr[e[1]].append(e[0])
    
    while queue:    
        q = queue.pop(0)
        for x in arr[q]:
            if visited[x] == -1:
                visited[x] = visited[q] + 1
                queue.append(x)
        
    answer = 0
    for x in visited:
        if max(visited) == x:
            answer +=1
    return answer 
