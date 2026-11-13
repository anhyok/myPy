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

root = tk.Tk()
root.title("실시간 set 중복 검사 수도쿠")
root.config(bg="gray")

entries = []

def get_val(r, c):
    """특정 칸의 입력을 숫자로 안전하게 읽어오는 함수"""
    val = entries[r][c].get().strip()
    return int(val) if val.isdigit() and len(val) == 1 else 0

def on_key_release(r, c):
    """키 입력 시 set을 활용해 실시간으로 중복을 검사하는 핵심 함수"""
    entry = entries[r][c]
    val_str = entry.get().strip()

    # 빈칸일 경우 기본 흰색으로 복구
    if not val_str:
        entry.config(bg="white", fg="black")
        return

    # 1~9 숫자가 아니거나 2자리 이상 입력 시 경고
    if not val_str.isdigit() or val_str == "0" or len(val_str) > 1:
        entry.config(bg="#ffdddd", fg="red")
        return

    num = int(val_str)

    # 1. 현재 칸(r, c)을 제외한 행(Row) 숫자들의 set
    row_set = {get_val(r, i) for i in range(9) if i != c} - {0}

    # 2. 현재 칸(r, c)을 제외한 열(Column) 숫자들의 set
    col_set = {get_val(i, c) for i in range(9) if i != r} - {0}

    # 3. 현재 칸(r, c)을 제외한 3x3 박스(Box) 숫자들의 set
    br, bc = (r // 3) * 3, (c // 3) * 3
    box_set = {get_val(i, j) for i in range(br, br + 3) for j in range(bc, bc + 3) if (i, j) != (r, c)} - {0}

    # 4. 세 영역의 집합을 하나로 합침 (합집합 | 연산)
    used_numbers = row_set | col_set | box_set

    # 5. 입력한 숫자가 이미 사용된 숫자 집합에 포함되어 있는지 확인
    if num in used_numbers:
        # 중복 발생: 빨간색 배경
        entry.config(bg="#ffdddd", fg="red")
    else:
        # 정상 입력: 연한 파란색 배경
        entry.config(bg="#e8f4f8", fg="#004085")

# UI 격자 생성
for r in range(9):
    row_entries = []
    for c in range(9):
        e = tk.Entry(root, width=3, font=("Arial", 16), justify="center")
        pad_y = (4, 1) if r % 3 == 0 and r != 0 else 1
        pad_x = (4, 1) if c % 3 == 0 and c != 0 else 1
        e.grid(row=r, column=c, padx=pad_x, pady=pad_y)
        
        if BOARD[r][c] != 0:
            e.insert(0, str(BOARD[r][c]))
            e.config(state="disabled")
        else:
            # 키를 누르고 뗄 때마다 on_key_release 함수 호출
            e.bind("<KeyRelease>", lambda event, r=r, c=c: on_key_release(r, c))
            
        row_entries.append(e)
    entries.append(row_entries)

root.mainloop()