def solution(land):
    row = 1
    
    while row < len(land):
        for i in range(4):
            land[row][i] += max(land[row-1][(i+1)%4],land[row-1][(i+2)%4],land[row-1][(i+3)%4])
        row += 1                
                
    return max(land[row-1])