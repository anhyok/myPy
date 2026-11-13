import tkinter as tk
from tkinter import messagebox

# 0은 빈칸
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

ANSWER = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7 ,9] 
]

window = tk.Tk()
window.title("SUDOKU")
window.config(bg="gray") # [추가] 배경색을 두어 여백이 테두리처럼 보이게 설정

entries = []
for r in range(9):
    row_entries = []
    for c in range(9):
        e = tk.Entry(window, width=3, font=("Arial", 16), justify="center")

        # [추가] 3x3 구분 여백: 3, 6번째 행/열의 위쪽과 왼쪽에 더 넓은 여백(4px) 부여
        pad_y = (4, 1) if r % 3 == 0 and r != 0 else 1
        pad_x = (4, 1) if c % 3 == 0 and c != 0 else 1

        e.grid(row=r, column=c, padx=pad_x, pady=pad_y)

        if BOARD[r][c] != 0:
            e.insert(0, str(BOARD[r][c]))
            e.config(state="disabled")

        row_entries.append(e)
    entries.append(row_entries)


def check():
    # 1. 화면 입력을 2차원 리스트(board)로 변환
    board = []
    for r in range(9):
        row_vals = []
        for c in range(9):
            val = entries[r][c].get().strip()
            if not val.isdigit() or not (1 <= int(val) <= 9):
                messagebox.showerror("오류", "1~9 사이의 숫자로 모든 빈칸을 채워주세요.")
                return
            row_vals.append(int(val))
        board.append(row_vals)

    # 2. set을 이용한 가로, 세로, 3x3 박스 검사
    for i in range(9):
        # 행(Row) 검사
        if len(set(board[i])) != 9:
            messagebox.showerror("오류", f"{i + 1}번째 행에 중복된 숫자가 있습니다!")
            return

        # 열(Column) 검사
        col = [board[r][i] for r in range(9)]
        if len(set(col)) != 9:
            messagebox.showerror("오류", f"{i + 1}번째 열에 중복된 숫자가 있습니다!")
            return

        # 3x3 박스(Box) 검사
        br, bc = (i // 3) * 3, (i % 3) * 3
        box = [board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
        if len(set(box)) != 9:
            messagebox.showerror("오류", f"3x3 영역({br+1}~{br+3}행)에 중복된 숫자가 있습니다!")
            return

    messagebox.showinfo("성공", "축하합니다! 수도쿠를 완벽하게 맞추셨습니다.")

# ANSWER을 이용하여 check() 함수가 정상작동하는지 확인
def test_answer():
    for r in range(9):
        for c in range(9):
            entries[r][c].delete(0, tk.END)
            entries[r][c].insert(0, str(ANSWER[r][c]))
    check()

tk.Button(window, text="정답 확인", command=check).grid(row=9, column=0, columnspan=9, pady=10)
tk.Button(window, text="테스트", command=test_answer).grid(row=9, column=7, columnspan=9, pady=10)

window.mainloop()