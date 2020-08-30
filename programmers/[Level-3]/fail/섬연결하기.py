def solution(n, costs):
    costs = [(c,a,b) for a,b,c in costs]
    costs.sort()
    visited = set()
    cyc = [me for me in range(n)]
    answer = 0
    
    def union(a,b):
        a = find(a)
        b = find(b)
        cyc[b] = a
    
    def find(a):    
        if cyc[a] == a:
            return a
        else:
            return find(cyc[a])

    for x in costs:
        if find(x[1]) != find(x[2]):
            visited.add(x[1])
            visited.add(x[2])
            answer += x[0]
            union(x[1],x[2])
            
    return answer

print(solution(4,	[[0,1,8],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

'''    
    def find(a):    
        if cyc[a] == a:
            return a
        else:
            return find(cyc[a])
'''