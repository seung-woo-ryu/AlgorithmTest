def solution(dirs):
    SET = set()
    pos = [0,0]
    moving = {'U': (0,1), 'D': (0,-1), 'L':(-1,0),'R':(1,0)}
    for move in dirs:
        x, y = moving[move]
        if -5 <= pos[0] + x and pos[0] + x <= 5 and -5 <= pos[1] + y and pos[1] + y <= 5:
            SET.add((pos[0],pos[1],pos[0] + x, pos[1] + y))
            SET.add((pos[0] + x, pos[1] + y,pos[0],pos[1]))
            pos[0] += x
            pos[1] += y
    
    return len(SET) // 2