'''
# https://devdoggo.netlify.app/post/alg_ds/challenges/longest_palindrome/

def longest_palindrome(s):
    """
        동적 프로그래밍 개념 이용
    """
    longest_palindrome = 0
    table = [[False for i in range(len(s))] for j in range(len(s))]

    # 다음과 같은 방식으로 테이블을 만든다:
    for i in range(len(s)):
        for j in range(len(s)-i):
            # len(substring) < 3 일 경우(다르게 표현하면, 두번째 대각선 줄을 만들 때까지)
            # substring의 끝이 같을 경우 True를 넣고, longest_palindrome 을 업데이트 한다
            if i < 2:
                if s[j] == s[i+j]:
                    table[j][i+j] = True
                    longest_palindrome = i+1
                else:
                    table[j][i+j] = False
            # len(substring) > 3 일 경우
            # substring의 끝이 같고, 왼쪽 밑 대각선 한칸에 있는 박스가 True면 True를 넣고, longest_palindrome을 업데이트 한다.
            else:
                if s[j] == s[i+j] and table[j+1][i+j-1]:
                    table[j][i+j] = True
                    longest_palindrome = i+1                    
                else:
                    table[j][i+j] = False
    return longest_palindrome

'''
def solution(s):
    n = len(s)
    arr = [[False for _ in range(n)] for _ in range(n)]
    
    lg_pa = 0
    
    for i in range(n):
        for j in range(i,-1,-1):
            if i - j < 2:
                if s[j] == s[i]:
                    arr[j][i] = True
            else:
                if arr[j+1][i-1] and s[j] == s[i]:
                    arr[j][i] = True
    
    for i in range(n-1, -1,-1):
        if i + 1 > lg_pa:
            for j in range(n):
                if arr[j][i]:
                    lg_pa = max(lg_pa,i-j+1)
                    break
        else:
            break
    
    return lg_pa
