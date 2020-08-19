import math

def solution(brown, yellow):
    answer = []
    B =(brown + 4)//2
    A = brown + yellow
    print(A,B)
    answer.append(int((B + math.sqrt(B**2 - 4*A))//2))
    answer.append(int((B - math.sqrt(B**2 - 4*A))//2))

    answer.sort(reverse=True)    
    return answer