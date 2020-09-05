def solution(N, road, K):
    INF = 9999999
    
    visited = [0,0] + [INF] * (N-1)
    arr = [[] for _ in range(N+1)]
    queue = []
    
    for frm, to, worth in road:
        arr[frm].append((worth,to,frm))
        arr[to].append((worth,frm,to))
    
    for i in arr[1]:
        queue.append(i)
    
    while queue:
        worth, to, frm= queue.pop(0)
        
        if visited[to] > visited[frm] + worth:
            visited[to] = visited[frm] + worth
            for x in arr[to]:
                queue.append(x)
    cnt = 0
    
    for i in visited:
        if K >= i:
            cnt += 1
    return cnt -1

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	,3))