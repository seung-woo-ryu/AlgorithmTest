def solution(answers):
    answer = []
    member = {1:[1,2,3,4,5,1,2,3,4,5], 2:[2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5], 3:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    
    mAnswer = {1:0,2:0,3:0}
    
    for i in range(len(answers)):
        if(answers[i] == member[1][i%len(member[1])]):
            mAnswer[1] = mAnswer[1] + 1
        if(answers[i] == member[2][i%len(member[2])]):
            mAnswer[2] = mAnswer[2] + 1
        if(answers[i] == member[3][i%len(member[3])]):
            mAnswer[3] = mAnswer[3] + 1
    
    mAnswer = sorted(mAnswer.items(), lambda x: x[1])
    
    answer.append(mAnswer[0])
    
    if(mAnswer[0] == mAnswer[1]):
        answer.append(mAnswer[1])
        if(mAnswer[1] == mAnswer[2]):
            answer.append(mAnswer[2])
        
    return answer