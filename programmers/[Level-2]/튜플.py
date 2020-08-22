import re

def solution(s):
    answer = []
    s = s.split('},')
    tmp = sorted(list(map(lambda x: set(re.findall('\d+', x)), s)),key=lambda x:len(x))
    answer.append(tmp[0])

    for i in range(len(tmp)-1):
        answer.append(tmp[i+1]- tmp[i])

    answer = list(map(list,answer))

    return [int(x[0]) for x in answer]