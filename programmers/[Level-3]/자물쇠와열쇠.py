def solution(key, lock):
    M, N = len(key), len(lock)
    K = 2*(M-1) + N
    li = [[-1 for _ in range(K)] for _ in range(K)]
    zeroCnt = 0

    for x in range(N):
        for y in range(N):
            if lock[x][y] == 1:
                li[M-1+x][M-1+y] = 1
            else:
                li[M-1+x][M-1+y] = 0
                zeroCnt += 1

    def traverse(x,y):
        cnt = 0
        for i in range(M):
            for j in range(M):
                if li[x+i][y+j] != -1:
                    if li[x+i][y+j] == 1 and key[i][j] == 1:
                        return False
                    elif li[x+i][y+j] == 0 and key[i][j]== 1:
                        cnt  += 1
        if cnt == zeroCnt:
            return True

    for _ in range(4):
        for x in range(M-1+N):
            for y in range(M-1+N):
                if traverse(x,y):
                    return True
        key = [[key[i][j] for i in reversed(range(M))] for j in range(M)]
                         
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))