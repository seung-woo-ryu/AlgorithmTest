'''
    문제가 이상함
    0x000
    0x0x0
    0x0x0
    000x0
    인경우 답이 0임. 
    최단경로란게 무조건 위->아래, 왼->오른쪽으로만
    움직였을 때 경로의 경우의 수
    위의 예시처럼 물웅덩이가 최단경로 움직임을 방해한다면
    도달할 수 있는 경우의 수가 0임
'''

def solution(m, n, puddles):
    maps = [[0] *(m+1) for _ in range(n+1)]
    li = [[0] *(m+1) for _ in range(n+1)]

    for x,y in puddles:
        li[y][x] = 1

    maps[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i ==1 and j==1:
                continue
            if [j,i] in puddles:
                maps[i][j] = 0
            else:
                maps[i][j] += (maps[i-1][j]+maps[i][j-1])
    for x in li:
        print(x)
    return (maps[-1][-1] % 1000000007)

print(solution(8,5,[[3, 1],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[6,2]]))