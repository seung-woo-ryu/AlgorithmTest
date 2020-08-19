prime = list()
st = set()

def cal(numbers,s):
    global st

    for idx, num in enumerate(numbers):
        number = []
        st.add(int(s+num))
        number = numbers[:idx] + numbers[idx+1:]
        cal(number,s+num)
        
def solution(numbers):
    global prime
    cnt = 0
    n = 10 ** len(numbers)
    prime = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if prime[i] == True:           
            for j in range(i+i, n, i):
                prime[j] = False
    prime[1] = prime[0] = False
    cal(numbers,"")

    for i in list(st):
        if prime[i]:
            cnt +=1

    return cnt

print(solution("011"))