def solution(m, n, board):
    board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    answer = 0
    li = set()
    print(board)
    while True:
        for row in range(len(board) - 1):
            for col in range(len(board[row]) - 1):
                if len(board[row+1]) <= col + 1:
                    break
                elif board[row][col] == board[row][col+1] == board[row+1][col] == board[row+1][col+1]:
                    li.add((row,col))
                    li.add((row,col+1))
                    li.add((row+1,col))
                    li.add((row+1,col+1))
        print(sorted(li))
        if not len(li):
            return answer
        for x, y in reversed(sorted(li)):
            board[x].pop(y)
            answer += 1
        li = set()