def solution(nodeinfo):
    nodeinfo = [[y,x,idx+1] for idx,(x,y) in enumerate(nodeinfo)]
    nodeinfo.sort(key = lambda x: (-x[0],x[1]))
    li = dict()
    # (번호, x좌표)
    li[1] = [nodeinfo[0][2],nodeinfo[0][1]]
    
    for idx in range(1,len(nodeinfo)):
        pos = 1
        while True:
            if pos in li:
                pos =2*pos + ( 1 if li[pos][1] < nodeinfo[idx][1] else 0)
            else:
                li[pos] = [nodeinfo[idx][2],nodeinfo[idx][1]]
                break
                
    pre = []
    def preorder(i):
        if i in li:
            pre.append(li[i][0])
            preorder(2*i)
            preorder(2*i + 1)
    preorder(1)
    post = []
    def postorder(i):
        if i in li:
            postorder(2*i)
            postorder(2*i + 1)
            post.append(li[i][0])
    postorder(1)

    return [pre,post]

print(solution([[1,2]]))