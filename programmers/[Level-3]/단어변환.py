CNT = 1000000
toggle = False

def isSim(A,B):
    cnt = 0
    for i in range(len(A)):
        if A[i] == B[i]:
            cnt += 1

    if cnt == len(A) - 1:
        return True
    else:
        return False
        

        
def solution(begin, target, words):
    global CNT
    global toggle
    if target not in words:
        return 0
    
    def dfs(startWord, new_set, cnt,li):
        global CNT
        global toggle
        for targetWord in list(new_set):
            if isSim(startWord, targetWord):
                if target == targetWord:
                    CNT = min(CNT, cnt + 1)
                    toggle = True
                else:
                    tmp_set = new_set - {targetWord}
                    dfs(targetWord, tmp_set, cnt+1,li)
    
    dfs(begin,set(words), 0,[begin])

    if toggle:
        return CNT    
    else:
        return 0