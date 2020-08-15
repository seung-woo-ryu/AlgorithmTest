def solution(n, arr1, arr2):
    
    answer = []
    
    for index, value in enumerate(arr1):
        value = int(value)
        tmp = ""
        for i in range(n-1,-1,-1):
            if 2 ** i <= value:
                tmp = tmp + "1"
                value = int(value - 2 ** i)
            else:
                tmp = tmp + "0"
        arr1[index] = tmp
        print(tmp)
    
    for index, value in enumerate(arr2):
        value = int(value)
        tmp = ""
        for i in range(n-1,-1,-1):
            if 2 ** i <= value:
                tmp = tmp + "1"
                value = int(value - 2 ** i)
            else:
                tmp = tmp + "0"
        arr2[index] = tmp                
        print(tmp)
    
    for x in range(n):
        tmp = ""
        for y in range(n):
            tmp = tmp + ("#" if (arr1[x][y] == "1" or arr2[x][y] == "1") else " ")
        answer.append(tmp)
    
    return answer
