from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]
    # k를 찌르는 노드 갯수
    node2k = defaultdict(int)
    # k가 찌르는 노드 갯수
    k2node = defaultdict(int)
    
    for frm, to in edges:
        node2k[frm] += 0
        node2k[to] += 1
        k2node[frm] += 1
        k2node[to] += 0
    
    for k, v in node2k.items():
        if node2k[k] == 0 and k2node[k] > 1:
            answer[0] = k
        if k2node[k] == 0:
            answer[2] += 1
        if k2node[k] == 2 and (node2k[k] == 2 or node2k[k] == 3):
            answer[3] += 1
            
    answer[1] = k2node[answer[0]] - (answer[2]+answer[3])
    
    return answer