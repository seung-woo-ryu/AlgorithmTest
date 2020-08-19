def div(p):
    cnt = 1 if p[0] == '(' else -1
    
    for i in range(1,len(p)):
        cnt += 1 if p[i] == '(' else -1
        if cnt == 0:
            return p[0:i+1], p[i+1:]
        
def check(p):
    cnt = 0
    for x in p:
        cnt += 1 if x == '(' else -1
        if cnt < 0:
            return False
    
    return True

def solution(p):
    answer = ''
    
    if len(p) == 0:
        return answer
    
    answer = p
    
    u,v = div(p)

    if check(u):
        return u + solution(v)

    else:
        tmp = "(" + solution(v) + ")"
        u = u[1:len(u) - 1]
        ch = ""
        for x in u:
            ch += ")" if x =="(" else "("
        tmp += ch
        
    return tmp

