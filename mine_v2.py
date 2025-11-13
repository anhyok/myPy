##col, row = [3, 3]
##matrix = [['.', '*', '*'],
##          ['*', '.', '.'],
##          ['.', '*', '.']]

col, row = [5, 5]
matrix = [['.', '.', '*', '.', '.'],
          ['.', '.', '.', '*', '.'],
          ['.', '*', '.', '.', '.'],
          ['.', '*', '*', '*', '.'],
          ['*', '.', '*', '.', '.']]


##col, row = map(int, input().split())
##matrix = []
##for i in range(row):
##    matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.': #if it's NOT bomb X)
            bomb = 0
            #count the BOMBs around me
            checkpoints = [
                [i-1,j-1], [i-1,j],    [i-1, j+1],
                [i,j-1],   [i,j],      [i, j+1],
                [i+1,j-1], [i+1,j],    [i+1, j+1]
            ]
            for x, y in checkpoints:
                if not (0<=x<row and 0<=y<col):
                    continue
                if matrix[x][y]=='*':                    
                    bomb += 1
            print(bomb, end='')
        else: #just print if it's BOMB :)
            print(matrix[i][j], end='')
    print()