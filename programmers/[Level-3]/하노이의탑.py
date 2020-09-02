def solution(n):
    answer = []  
    
    def move(start, mid, to,n):
        if n == 1:
            answer.append([start,to])
        else:
            move(start,to,mid,n-1)
            answer.append([start,to])
            move(mid,start,to,n-1)
    
    move(1,2,3,n)
    return answer