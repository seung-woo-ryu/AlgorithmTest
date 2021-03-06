class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix) == 0: return
        self.cdf = [[0]*(len(matrix[0]) + 1) for x in range(len(matrix)+1)]
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.cdf[i][j] = self.cdf[i-1][j] + self.cdf[i][j-1] - self.cdf[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.cdf[row2+1][col2+1] - self.cdf[row1][col2+1] - self.cdf[row2+1][col1] + self.cdf[row1][col1]
