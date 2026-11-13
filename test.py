row,col=map(int,input().split())

matrix=[]
for i in range(row):
    matrix.append(list(input()))

result = [['']*col for i in range(row)]

for i in range(row):
    for j in range(col):
        if matrix[i][j] == '*':
            result[i][j] = '*'
        else:
            count=0


            if i > 0:
                if j>0 and matrix[i-1][j-1] == '*':   
                    count += 1
                if matrix[i-1][j] == '*':
                    count += 1
                if j < col-1 and matrix[i-1][j+1] == '*':     
                    count += 1

            if j > 0 and matrix[i][j-1] == '*':    
                count += 1
            if j < col - 1 and matrix[i][j+1] == '*':     
                count += 1

            if i < row - 1:    
                if j > 0 and matrix[i+1][j-1] == '*':    
                    count += 1
                if matrix[i+1][j] == '*':            
                    count += 1
                if j < col - 1 and matrix[i+1][j+1] == '*':    
                    count += 1

            result[i][j] = str(count)  

for i in range(row):                
    print(''.join(result[i]))
