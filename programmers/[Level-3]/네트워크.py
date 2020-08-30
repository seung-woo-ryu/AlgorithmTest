visited = []

def dfs(i, computers):
    global visited
    for j in range(len(computers)):
        if  visited[j] == False and computers[i][j] == 1:
            visited[j] = True
            dfs(j,computers)
    
def solution(n, computers):
    global visited
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i, computers)
            answer += 1
    
    return answer