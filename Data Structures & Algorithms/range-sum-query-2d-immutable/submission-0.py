class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix= matrix #[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r_start,r_end= row1,row2 #1,2
        c_start,c_end= col1,col2 #1,2
        rsum=0
        for r in range(len(self.matrix)): # 0,1,2
            if r >= r_start and r <= r_end: # 1>=1 and 1<=2
                for c in range(len(self.matrix[r])): # [1,1,1,1,1]
                    if c >= c_start and c <= c_end:  # 1>=1 and 1<=2
                        rsum+= self.matrix[r][c] #[1][1] + [1,2] + [2][1] + [2][2]
        return rsum





        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)