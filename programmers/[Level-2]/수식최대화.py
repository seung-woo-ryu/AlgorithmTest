from itertools import permutations
import copy

def solution(expression):
    answer = 0
    li = []
    li3 = []
    tmp = ""
    for x in expression:
        if x in "-+*":
            li.append(x)
    li = list(set(li))
    
    for e in expression:
        if str.isdigit(e):
            tmp += e
        else:
            li3.append(int(tmp))
            li3.append(e)
            tmp = ""
    li3.append(int(tmp))
    
    for exp in list(permutations(li,len(li))):
        li2 = copy.deepcopy(li3)
        for exp2 in exp:
            i = 1
            while i < len(li2):
                if li2[i] == "+" and li2[i] == exp2:
                    li2[i-1]=li2[i-1] + li2[i+1]
                    del li2[i:i+2]
                elif li2[i] == "-" and li2[i] == exp2:
                    li2[i-1]=li2[i-1] - li2[i+1]
                    del li2[i:i+2]
                elif li2[i] == "*" and li2[i] == exp2:
                    li2[i-1]=li2[i-1] * li2[i+1]
                    del li2[i:i+2]
                else:
                    i += 2
        li2[0] *= - 1 if li2[0] < 0 else 1
        answer = max(answer, li2[0])
    
    return answer