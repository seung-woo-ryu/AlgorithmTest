def solution(genres, plays):
    di = dict()
    di2 = dict()
    answer = []
    
    for idx, genre in enumerate(genres):
        if genre in di:
            di[genre] += plays[idx]
            di2[genre].append((plays[idx],idx))
        else:
            di[genre] = plays[idx]
            di2[genre] = [(plays[idx],idx)]   
    
    
    li = sorted(di.items(), key = lambda x: x[1], reverse= True)

    for x in di2.keys():
        di2[x] = sorted(di2[x], key=lambda X:(-X[0],X[1]))
    
    for name in li:
        for idx, pos in enumerate(di2[name[0]]):
            if idx <2:
                answer.append(pos[1])        
        
    return answer