import math

BOARD_SIZE = 9
WIN_LINE = 5
MAX_DEPTH = 3

game_board: str = '_' * (BOARD_SIZE * BOARD_SIZE)

AI = True 
HUMAN = False 

AI_MARK = 'X' 
HUMAN_MARK = 'O' 

def main(): 
    global game_board
    player: bool = HUMAN # AI가 후공으로 시작하도록 설정 (HUMAN이 먼저 두도록), AI가 선공으로 시작하려면 player = AI로 변경
    
    print(f'\n{BOARD_SIZE}x{BOARD_SIZE} 오목 게임을 시작합니다.') 
    print("※ 좌표 입력 방식: [세로행(1~9)][가로열(1~9)] 연속 입력 (예: 맨 왼쪽 아랫칸은 11, 정중앙은 55)")
    draw() 
    
    while find_empty(game_board) and not is_end(game_board): 
        if player == AI: 
            print("AI가 엄격하게 계산 중입니다...", end="", flush=True)
            
            empty_count = len(find_empty(game_board))
            if empty_count == BOARD_SIZE * BOARD_SIZE:
                position = (BOARD_SIZE // 2) * BOARD_SIZE + (BOARD_SIZE // 2)
            else:
                position, _ = minimax(game_board, MAX_DEPTH, float('-inf'), float('inf'), AI) 
            
            if position == -1:
                position = get_candidate_moves(game_board)[0]
                
            print(f"\nAI가 선택한 위치: {position // BOARD_SIZE + 1}{position % BOARD_SIZE + 1}")
            place(position, AI_MARK) 
            player = HUMAN 
        else: 
            position = input_num() 
            place(position, HUMAN_MARK) 
            player = AI 
        draw() 
    ending() 


def find_empty(board: str) -> tuple[int, ...]: 
    return tuple(x for x, cell in enumerate(board) if cell == '_') 


def get_candidate_moves(board: str) -> list[int]:
    size = BOARD_SIZE
    candidates = {}
    
    for i, cell in enumerate(board):
        if cell != '_':
            r, c = i // size, i % size
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < size and 0 <= nc < size:
                        idx = nr * size + nc
                        if board[idx] == '_':
                            candidates[idx] = candidates.get(idx, 0) + 1
                            
    sorted_candidates = sorted(candidates.keys(), key=lambda x: candidates[x], reverse=True)
    return sorted_candidates if sorted_candidates else [size * (size // 2) + (size // 2)]


def is_end(board: str) -> bool: 
    return is_win(board, AI_MARK) or is_win(board, HUMAN_MARK) 


def is_win(board: str, player: str) -> bool:
    size = BOARD_SIZE
    for r in range(size):
        for c in range(size - WIN_LINE + 1):
            if all(board[r * size + c + i] == player for i in range(WIN_LINE)): return True
    for r in range(size - WIN_LINE + 1):
        for c in range(size):
            if all(board[(r + i) * size + c] == player for i in range(WIN_LINE)): return True
    for r in range(size - WIN_LINE + 1):
        for c in range(size - WIN_LINE + 1):
            if all(board[(r + i) * size + (c + i)] == player for i in range(WIN_LINE)): return True
    for r in range(size - WIN_LINE + 1):
        for c in range(WIN_LINE - 1, size):
            if all(board[(r + i) * size + (c - i)] == player for i in range(WIN_LINE)): return True
    return False


def check_line_score(line_str: str) -> int:
    score = 0
    if "XXXXX" in line_str: score += 100000
    elif "_XXXX_" in line_str: score += 5000
    elif "XXXX_" in line_str or "_XXXX" in line_str: score += 1000
    elif "_XXX_" in line_str: score += 800
    elif "XX_XX" in line_str or "X_XXX" in line_str or "XXX_X" in line_str: score += 500
    elif "_XX_" in line_str: score += 50
    
    if "OOOOO" in line_str: score -= 100000
    elif "_OOOO_" in line_str: score -= 50000
    elif "OOOO_" in line_str or "_OOOO" in line_str: score -= 8000
    elif "_OOO_" in line_str: score -= 4000
    elif "OO_OO" in line_str or "O_OOO" in line_str or "OOO_O" in line_str: score -= 2000
    elif "_OO_" in line_str: score -= 100
    return score


def evaluate(board: str) -> int: 
    if is_win(board, AI_MARK): return 500000
    if is_win(board, HUMAN_MARK): return -500000
    size = BOARD_SIZE
    score = 0
    for r in range(size):
        row_str = board[r * size : (r + 1) * size]
        score += check_line_score(row_str)
    for c in range(size):
        col_str = "".join(board[r * size + c] for r in range(size))
        score += check_line_score(col_str)
    for d in range(-size + 1, size):
        diag = "".join(board[r * size + (r - d)] for r in range(size) if 0 <= r - d < size)
        if len(diag) >= 5: score += check_line_score(diag)
    for d in range(2 * size):
        diag = "".join(board[r * size + (d - r)] for r in range(size) if 0 <= d - r < size)
        if len(diag) >= 5: score += check_line_score(diag)
    return score


def minimax(board: str, depth: int, alpha: float, beta: float, max_player: bool) -> tuple: 
    if is_win(board, AI_MARK) or is_win(board, HUMAN_MARK) or depth == 0 or not find_empty(board): 
        return -1, evaluate(board) 
        
    position = -1 
    choices = get_candidate_moves(board)
    
    if max_player == AI: 
        value = float('-inf') 
        for each in choices: 
            next_board = board[:each] + AI_MARK + board[each + 1:]
            _, score = minimax(next_board, depth - 1, alpha, beta, HUMAN) 
            if score > value: 
                value = score 
                position = each 
            alpha = max(alpha, value)
            if beta <= alpha: break 
        return position, value 
    else: 
        value = float('inf') 
        for each in choices: 
            next_board = board[:each] + HUMAN_MARK + board[each + 1:]
            _, score = minimax(next_board, depth - 1, alpha, beta, AI) 
            if score < value: 
                value = score 
                position = each 
            beta = min(beta, value)
            if beta <= alpha: break 
        return position, value 


def place(x: int, player: str) -> bool: 
    if is_valid(x): 
        global game_board 
        game_board = game_board[:x] + player + game_board[x + 1:] 
        return True 
    return False 


def is_valid(x: int) -> bool: 
    return x in find_empty(game_board) 

def input_num() -> int: 
    while True: 
        input_str = input('\n위치 선택 (11 ~ 99)? ').strip()
        
        # 1. 두 자릿수 숫자인지 검증
        if len(input_str) == 2 and input_str.isdecimal():
            row = int(input_str[0])  # 십의 자리 (세로 행)
            col = int(input_str[1])  # 일의 자리 (가로 열)
            
            # 2. 각 자릿수가 1~9 범위 안에 있는지 검증 (0 입력 차단)
            if 1 <= row <= 9 and 1 <= col <= 9:
                # 3. 2차원 좌표를 내부 1차원 인덱스(0~80)로 변환
                num = (row - 1) * BOARD_SIZE + (col - 1)
                
                if num in find_empty(game_board): 
                    return num 
                    
        print("잘못된 입력이거나 이미 돌이 놓인 자리입니다. 11~99 사이의 올바른 좌표를 입력해주세요.") 


def draw(): 
    size = BOARD_SIZE
    print(f"\n--- 현재 {size}x{size} 오목판 상태 (가로/세로 좌표계) ---")
    
    for r in range(size - 1, -1, -1):
        idx_start = r * size
        idx_end = (r + 1) * size
        
        # 실제 돌 배치 상태 문자열 가공
        board_row = "  ".join(game_board[idx_start:idx_end])
        
        # [세로행][가로열] 가이드 가공 (r+1이 십의자리, c+1이 일의자리)
        key_row = " ".join(f"{(r+1)*10 + (c+1)}" for c in range(size))
        
        print(f"행 {r+1} |  {board_row}   |   {key_row}")
    
    # 밑면에 가로 열 번호 가이드 추가
    print("        " + "=  "*size + " |   " + "== "*size)
    print("열      " + "  ".join(str(c+1) for c in range(size)) + "   |    " + "  ".join(str(c+1) for c in range(size)))
    print("---------------------------------------------------------")
    
    
def ending(): 
    if is_win(game_board, AI_MARK): 
        print('AI Win (5목 완성)') 
    elif is_win(game_board, HUMAN_MARK): 
        print('HUMAN Win (5목 완성)') 
    else: 
        print('Tie') 


if __name__ == '__main__': 
    main()