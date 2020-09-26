def solution(sticker):
    
    n = len(sticker)
    if n <= 2:
        return max(sticker)

    li = [0] * n
    li[0] = sticker[0]
    li[1] = max(sticker[0],sticker[1])
    
    for i in range(2,n-1):
        li[i] = max(li[i-2] + sticker[i],li[i-1])
    
    li2 = [0] * n
    li2[0] = 0
    li2[1] = sticker[1]
    
    for i in range(2,n):
        li2[i] = max(li2[i-2] + sticker[i],li2[i-1])
        
    return max(max(li),max(li2))