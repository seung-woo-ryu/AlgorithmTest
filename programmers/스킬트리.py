def solution(skill, skill_trees):
    answer = 0
    
    for examWord in skill_trees:
        prePos = -2
        toggle = True
        for i in range(len(skill)):
            curPos = examWord.find(skill[i])
            if (prePos > curPos and curPos != -1) or (prePos == -1 and curPos != -1):
                toggle = False
                break
            prePos = curPos
        if toggle:
            answer += 1

    return answer
