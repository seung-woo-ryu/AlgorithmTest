cnt = 0

def cal(numbers,i,target,now) :
    global cnt
    
    if i == len(numbers)- 1:
        if now + numbers[i] == target:
            cnt += 1
        if now + numbers[i] * -1== target:
            cnt += 1
    else:
        cal(numbers,i+1,target,now+numbers[i])
        cal(numbers,i+1,target,now+numbers[i] * -1)

def solution(numbers, target):
    cal(numbers,0,target,0)
    return cnt
