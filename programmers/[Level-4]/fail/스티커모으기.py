vi = []
li2 = []
answer = 0

def s(n,edges):
    global answer
    global vi

    li2 = [[0 for _ in range(n)] for _ in range(n)]

    vi = [0] * n
    def re(idx,li2):
        global vi
        if idx != 0:
            for i in range(0,idx):
                if li2[idx][i] == 1:
                    vi[i] += 1
                    break
            re(i,li2)

    for x,y in edges:
        li2[x][y] = 1
        li2[y][x] = 1
    
    for x,y in edges:
        if x!= 0:
            vi[x] += 1
            re(x,li2)

    queue = []
    temp = set()
    temp.add(0)

    answer= 0
    
    while temp:
        for x in list(temp):
            for i in range(x+1,n):
                if li2[x][i] == 1:
                    queue.append(i)
        max_index = -1
        max_value =-1
        for x in queue:
            max_temp=0
            for k in range(x+1,n):
                max_temp = max(max_temp,vi[k])

            if vi[x] - max_temp > max_value:
                max_index  = x
                max_value = vi[x] - max_temp
        temp = set(queue) - set([max_index])

    return n - answer

print(s(19,	[[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]))