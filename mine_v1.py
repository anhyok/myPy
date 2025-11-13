row, col = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in range(row):
    for j in range(col):        
        if matrix[i][j] == '.':
            mine = 0
            if 0<=i-1<col and 0<=j-1<row and matrix[i-1][j-1] == '*':
                mine += 1
            if 0<=i-1<col and 0<=j<row and matrix[i-1][j] == '*':
                mine += 1
            if 0<=i-1<col and 0<=j+1<row and matrix[i-1][j+1] == '*':
                mine += 1
            if 0<=i<col and 0<=j-1<row and matrix[i][j-1] == '*':
                mine += 1
            if 0<=i<col and 0<=j+1<row and matrix[i][j+1] == '*':
                mine += 1
            if 0<=i+1<col and 0<=j-1<row and matrix[i+1][j-1] == '*':
                mine += 1
            if 0<=i+1<col and 0<=j<row and matrix[i+1][j] == '*':
                mine += 1
            if 0<=i+1<col and 0<=j+1<row and matrix[i+1][j+1] == '*':
                mine += 1            
            print(mine, end='')
            mine=0
        else:
            print(matrix[i][j], end='')
    print()