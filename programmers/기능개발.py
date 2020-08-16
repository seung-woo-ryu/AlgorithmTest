import math

def solution(progresses, speeds):
    finish = list()
    cnt = list()
    answer = []
    
    for i in range(len(progresses)):
        n = math.ceil((100 - progresses[i]) / speeds[i])
        finish.append(n)
    
    for i in finish:
        if len(cnt) == 0:
            cnt.append(i)
        else:
            if cnt[0] >= i:
                cnt.append(i)
            else:
                answer.append(len(cnt))
                del cnt[:]
                cnt.append(i)

    if(len(cnt) !=0):
        answer.append(len(cnt))

    return answer
