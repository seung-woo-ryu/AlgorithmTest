'''
    Hint
    (1) 3씩 올라간다는 점에서 3진법과 비슷
    (2) but, 3으로 떨어지는 수일 때는 3진법과 다름. ex) 6(10진) = 20(3진) = 14(124나라)
        인걸로 보아 
'''

def solution(n):
    answer = ""
    while n:
        n, nam = divmod(n,3)
        answer = "412"[nam]+ answer
        if nam == 0:
            n -= 1
        
    return answer
