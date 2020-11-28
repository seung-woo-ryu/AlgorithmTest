class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])
        
        def convert(r):
            for c in range(1, col):
                A[r][c] = 0 if A[r][c] == 1 else 1
            
        for r in range(row):
            if A[r][0] == 0:
                convert(r)
        
        answer = row * 2**(col-1)        
        
        for c in range(1,col):
            oneCnt = 0
            for r in range(row):
                if A[r][c] == 1:
                    oneCnt += 1
            twoCnt = oneCnt if oneCnt > row//2 else row - oneCnt
            answer += twoCnt * 2**(col-1-c)
        
        return answer
                