def check_bomb(matrix, x, y): #check how many bombs around me
    bomb = 0
    checkpoints = [
        [x-1,y-1], [x-1,y],    [x-1, y+1],
        [x,y-1],   [x,y],      [x, y+1],
        [x+1,y-1], [x+1,y],    [x+1, y+1]
    ]
    for x, y in checkpoints:
        if not (0<=x<row and 0<=y<col):
            continue
        if matrix[x][y]=='*':                    
            bomb += 1
    return bomb

col, row = map(int, input().split())
matrix = []
for i in range(row):
   matrix.append(list(input()))

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.': #if it's NOT bomb X)
            print(check_bomb(matrix, i, j), end='')
        else: #just print if it's BOMB :)
            print(matrix[i][j], end='')
    print()