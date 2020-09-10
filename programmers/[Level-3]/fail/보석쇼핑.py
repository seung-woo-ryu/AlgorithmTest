def solution(gems):
    gem_kind = len(set(gems))
    length = len(gems)
    start, end = 0, -1
    cnt = 0
    answer = [0,10000000]
    dic = dict()
    for x in (set(gems)):
        dic[x] = 0
    
    satisfy = False
    
    while True:
        if not satisfy:
            end += 1
            if end == length:
                break
            dic[gems[end]] += 1
            if dic[gems[end]] == 1:
                cnt += 1
                if cnt == gem_kind:
                    satisfy = True
                    if answer[1] - answer[0] > end - start:
                        answer[1], answer[0] = end +1, start+1
        else:
            start += 1
            if start == length:
                break
            dic[gems[start-1]] -=1
            if dic[gems[start-1]] == 0:
                cnt -=1
                satisfy = False
                continue
            if answer[1] - answer[0] > end - start:
                answer[1], answer[0] = end +1, start+1
                
    return answer