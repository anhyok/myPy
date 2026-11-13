import tkinter as tk
import random

# 게임 보드 및 블록 설정
ROWS = 20
COLS = 10
CELL_SIZE = 30  # 한 칸의 픽셀 크기

# 테트로미노 모양 정의 (상대 좌표계)
SHAPES = {
    'I': [(0, -1), (0, 0), (0, 1), (0, 2)],
    'J': [(-1, -1), (-1, 0), (0, 0), (1, 0)],
    'L': [(1, -1), (-1, 0), (0, 0), (1, 0)],
    'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
    'S': [(0, 0), (1, 0), (-1, 1), (0, 1)],
    'T': [(0, -1), (-1, 0), (0, 0), (1, 0)],
    'Z': [(-1, 0), (0, 0), (0, 1), (1, 1)]
}

COLORS = {
    'I': 'cyan', 'J': 'blue', 'L': 'orange', 'O': 'yellow',
    'S': 'green', 'T': 'purple', 'Z': 'red'
}

class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Tkinter Tetris")
        
        # 1. 게임 상태 변수 초기화
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]  # 2차원 행렬 보드 [cite: 13]
        self.total_cleared_rows = 0  # 누적 지운 줄 수 [cite: 49]
        self.init_speed = 1000       # 초기 하강 속도 (1초) [cite: 47]
        self.current_speed = self.init_speed
        self.game_over = False
        
        # 2. UI 레이아웃 구성 (메인 화면 & 우측 점수판 분리)
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)
        
        # 테트리스 격자판 Canvas 생성
        self.canvas = tk.Canvas(self.main_frame, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg='black')
        self.canvas.pack(side=tk.LEFT)
        
        # 점수판 Label 생성 [cite: 4]
        self.score_label = tk.Label(self.main_frame, text=f"Lines: {self.total_cleared_rows}\nSpeed: {self.current_speed}ms", 
                                    font=("Arial", 14), justify=tk.LEFT)
        self.score_label.pack(side=tk.RIGHT, padx=20, fill=tk.Y)
        
        # 3. 키보드 이벤트 바인딩 [cite: 31, 61]
        self.root.bind("<Left>", lambda event: self.move(-1, 0))
        self.root.bind("<Right>", lambda event: self.move(1, 0))
        self.root.bind("<Down>", lambda event: self.move_down_event())  # 아래 방향키 강제 하강 [cite: 53]
        self.root.bind("<Up>", lambda event: self.rotate_block())
        self.root.bind("<space>", lambda event: self.hard_drop())       # 스페이스바 즉시 하강 [cite: 53]
        
        # 4. 게임 시작
        self.create_new_block()
        self.auto_drop_loop()  # 자동 하강 루프 시작 

    def create_new_block(self):
        """새로운 블록을 생성하고 중앙 상단에 배치합니다."""
        self.current_type = random.choice(list(SHAPES.keys()))
        self.current_shape = list(SHAPES[self.current_type])
        self.current_x = COLS // 2
        self.current_y = 1
        
        # 블록 생성 직후 충돌하면 게임 오버 [cite: 5]
        if not self.is_valid_move(self.current_shape, self.current_x, self.current_y):
            self.game_over = True
            self.canvas.create_text(COLS*CELL_SIZE//2, ROWS*CELL_SIZE//2, 
                                    text="GAME OVER", fill="white", font=("Arial", 24, "bold"))

    def is_valid_move(self, shape, offset_x, offset_y):
        """블록이 벽이나 바닥, 기존 블록과 충돌하는지 검사합니다[cite: 18]."""
        for dx, dy in shape:
            nx, ny = offset_x + dx, offset_y + dy
            if nx < 0 or nx >= COLS or ny >= ROWS:
                return False  # 벽이나 바닥 탈출 [cite: 18]
            if ny >= 0 and self.board[ny][nx] != 0:
                return False  # 기존 고정된 블록과 충돌 [cite: 18]
        return True

    def move(self, dx, dy):
        """블록을 좌/우/아래로 이동시킵니다."""
        if self.game_over: return False
        
        if self.is_valid_move(self.current_shape, self.current_x + dx, self.current_y + dy):
            self.current_x += dx
            self.current_y += dy
            self.draw_scene()
            return True
        return False

    def move_down_event(self):
        """아래 방향키(Down) 입력 시 한 칸 강제 하강 처리 및 화면 갱신[cite: 53, 57]."""
        self.move(0, 1)

    def hard_drop(self):
        """스페이스바 입력 시 바닥까지 즉시 떨어뜨리고 고정합니다[cite: 53, 55]."""
        if self.game_over: return
        
        # 바닥에 닿을 때까지 Y 좌표를 증가 [cite: 56]
        while self.is_valid_move(self.current_shape, self.current_x, self.current_y + 1):
            self.current_y += 1
            
        self.freeze_block()  # 고정 [cite: 56]
        self.draw_scene()    # 즉시 화면 렌더링 동기화 [cite: 63, 66]

    def rotate_block(self):
        """시계 방향 회전 연산 (-y, x) 선형 변환[cite: 41]."""
        if self.game_over: return
        
        rotated = [(-dy, dx) for dx, dy in self.current_shape]  # 회전 공식 적용 [cite: 41]
        if self.is_valid_move(rotated, self.current_x, self.current_y):
            self.current_shape = rotated
            self.draw_scene()

    def freeze_block(self):
        """블록을 보드 데이터에 고정하고 줄 제거 및 새 블록 생성을 처리합니다[cite: 23]."""
        for dx, dy in self.current_shape:
            if self.current_y + dy >= 0:
                self.board[self.current_y + dy][self.current_x + dx] = self.current_type
        
        self.clear_rows()
        self.create_new_block()

    def clear_rows(self):
        """리스트 필터링을 사용하여 가득 찬 줄을 지우고 속도를 조절합니다[cite: 42]."""
        # 빈 공간(0)이 하나라도 있는 행만 필터링하여 남김 [cite: 42]
        new_board = [row for row in self.board if 0 in row]
        cleared = ROWS - len(new_board)
        
        if cleared > 0:
            # 사라진 줄 수만큼 상단에 빈 행([0]*COLS) 추가 [cite: 42]
            self.board = [[0 for _ in range(COLS)] for _ in range(cleared)] + new_board
            self.total_cleared_rows += cleared  # 실시간 누적 [cite: 49]
            
            # 줄 수 비례 동적 속도 계산 (최대 200ms 한계 제한) [cite: 50, 52]
            self.current_speed = max(200, self.init_speed - (self.total_cleared_rows * 50))
            self.score_label.config(text=f"Lines: {self.total_cleared_rows}\nSpeed: {self.current_speed}ms")

    def auto_drop_loop(self):
        """ontimer 대신 tkinter의 after()를 활용한 독립적인 하강 루프."""
        if not self.game_over:
            # 아래로 한 칸 내리기 시도, 실패하면 바닥에 닿은 것이므로 고정 [cite: 23]
            if not self.move(0, 1):
                self.freeze_block()
                self.draw_scene()
            
            # 지정된 밀리초(ms) 후에 다시 자기 자신을 호출 (재귀적 타이머 루프) [cite: 35]
            self.root.after(self.current_speed, self.auto_drop_loop)

    def draw_scene(self):
        """Canvas를 비우고 현재 보드 상태와 움직이는 블록을 새로 그립니다."""
        self.canvas.delete("all")  # 전체 화면을 지우는 대신 Canvas 내부 객체만 초기화
        
        # 1. 고정된 보드 블록 그리기
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c] != 0:
                    self.draw_cell(c, r, COLORS[self.board[r][c]])
                    
        # 2. 현재 조작 중인 활성화 블록 그리기
        if not self.game_over:
            for dx, dy in self.current_shape:
                self.draw_cell(self.current_x + dx, self.current_y + dy, COLORS[self.current_type])

    def draw_cell(self, x, y, color):
        """지정된 좌표에 테트리스 사각형 셀을 그리는 헬퍼 함수"""
        x1 = x * CELL_SIZE
        y1 = y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

# 메인 실행부
if __name__ == "__main__":
    root = tk.Tk()
    game = Tetris(root)
    root.mainloop()