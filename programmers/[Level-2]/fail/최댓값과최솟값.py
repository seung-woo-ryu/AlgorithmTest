def solution(s):
    s = s.split(" ")
    li =list(map(int, s))
    
    return str(min(li)) + ' ' + str(max(li))