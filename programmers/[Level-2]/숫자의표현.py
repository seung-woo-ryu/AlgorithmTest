'''
    #다른 사람 풀이
    def expressions(num):
        return len([i  for i in range(1,num+1,2) if num % i is 0])
    
    풀이법: 주어진 숫자의 홀수 약수 갯수를 구하면 정답.
    ex) 15
    1,3,5,15
    약수 1이면: 15가 1개 있는 경우
    약수 3이면: 5가 3개 있는 경우. 
                5 + 5 + 5이다. 이러면 양쪽 숫자에 -1, +1을 해주면 3,4,5
    약수 5이면: 3이 5개 있는 경우.
                3 + 3 + 3 + 3 + 3이다. 왼쪽 수에서 2,1를 뺴서 오른쪽에 더해주면, 1,2,3,4,5
    약수 15이면: 2n+1이므로, n, n+1로 나뉨.
'''

def solution(n):
    li = {0:0}
    reLi = {0:0}
    tmp = 0
    
    answer = 0
    for i in range(1,n+1):
        tmp += i
        li[i] = tmp
        reLi[tmp] = i
            
    for i in range(n, 1,-1):
        if li[i] < n:
            break
        elif li[i] - n in reLi:
            answer +=1
            
    return answer
