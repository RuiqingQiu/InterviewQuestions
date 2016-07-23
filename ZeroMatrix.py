# 1.8 Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
def ZeroMatrix(matrix, M, N):
    row_zero = []
    column_zero = []
    for i in range(0, M):
        for j in range(0, N):
            if matrix[i][j] == 0:
                row_zero.append(j)
                column_zero.append(i)
    for i in row_zero:
        zero_row(matrix,i)
    for i in column_zero:
        zero_column(matrix,i)
    return matrix
def zero_row(matrix, row):
    for i in range(0, len(matrix)):
        matrix[i][row] = 0

def zero_column(matrix, column):
    for i in range(0, len(matrix[0])):
        matrix[column][i] = 0



testMatrix = [[1,2,3,4], [5,6,7,8],[9,10,11,0]]
print ZeroMatrix(testMatrix, 3, 4)
