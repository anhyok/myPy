import tkinter as tk

BOARD = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

window = tk.Tk()
window.title("SUDOKU")
window.config(bg="gray")  # 배경색을 두어 여백이 테두리처럼 보이게 설정

entries = []
for r in range(9):
    row_entries = []
    for c in range(9):
        e = tk.Entry(window, width=3, font=("Arial", 16), justify="center")
        
        # 3, 6번째 행/열의 위쪽과 왼쪽에 더 넓은 여백(4px) 부여
        pad_y = (4, 1) if r % 3 == 0 and r != 0 else 1
        pad_x = (4, 1) if c % 3 == 0 and c != 0 else 1
        e.grid(row=r, column=c, padx=pad_x, pady=pad_y)
        
        if BOARD[r][c] != 0:
            e.insert(0, str(BOARD[r][c]))
            e.config(state="disabled")
            
        row_entries.append(e)
    entries.append(row_entries)

def check():
    for r in range(9):
        for c in range(9):
            val = entries[r][c].get()
            if not val.isdigit() or not (1 <= int(val) <= 9):
                tk.messagebox.showerror("오류", "1~9 사이의 숫자로 모든 빈칸을 채워주세요.")
                return
    tk.messagebox.showinfo("완료", "모든 칸을 작성했습니다!")

tk.Button(window, text="정답 확인", command=check).grid(row=9, column=0, columnspan=9, pady=10)

window.mainloop()