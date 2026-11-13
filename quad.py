def quad(answer, arr, start_row, end_row, start_col, end_col):
    f = arr[start_row][start_col]
    print("{}-{} {}-{}: {}".format(start_row, end_row, start_col, end_col, f))
    for row in range(start_row, end_row+1):
        for col in range(start_col, end_col+1):            
            print("[{}, {}]: {}".format(row, col, arr[row][col]))
            if f == arr[row][col]:
                continue
            else:
                height = end_row - start_row
                width = end_col - start_col
                quad(answer, arr, start_row, start_row+height//2, start_col, start_col+width//2)
                quad(answer, arr, start_row+height//2+1, end_row, start_col, start_col+width//2)
                quad(answer, arr, start_row, start_row+height//2, start_col+width//2+1, end_col)
                quad(answer, arr, start_row+height//2+1, end_row, start_col+width//2+1, end_col)
                return                        
    answer.append(f)
    print(">", answer)

def solution(arr):
    answer = []
    
    row = col = len(arr)-1
    quad(answer, arr, 0, row, 0, col)
            
    cnt_0 = answer.count(0)
    cnt_1 = len(answer) - cnt_0
    return [cnt_0, cnt_1]

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
