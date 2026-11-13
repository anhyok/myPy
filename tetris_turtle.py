import turtle
import random

# 게임 보드 설정 (가로 10칸, 세로 20칸, 한 칸은 20픽셀)
COLS, ROWS = 10, 20
PIXEL = 20

# 난이도 및 속도 제어 변수
INIT_SPEED = 1000       # 초기 속도: 1000ms (1초)
current_speed = INIT_SPEED
total_cleared_rows = 0  # 플레이어가 맞춘 총 줄 수

# 7가지 테트로미노 모양 정의
SHAPES = {
    'I': [(0, 0), (-1, 0), (1, 0), (2, 0)],
    'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
    'T': [(0, 0), (-1, 0), (1, 0), (0, 1)],
    'S': [(0, 0), (-1, 0), (0, 1), (1, 1)],
    'Z': [(0, 0), (1, 0), (0, 1), (-1, 1)],
    'J': [(0, 0), (-1, 0), (1, 0), (-1, 1)],
    'L': [(0, 0), (-1, 0), (1, 0), (1, 1)]
}
COLORS = ['cyan', 'yellow', 'purple', 'green', 'red', 'blue', 'orange']

# 게임 상태 데이터
board = [[0] * COLS for _ in range(ROWS)]

# 현재 조작 중인 블록 변수
current_shape = []
current_color = ""
current_x, current_y = 0, 0

def create_new_block():
    """새로운 블록을 상단 중앙에 생성합니다."""
    global current_shape, current_color, current_x, current_y
    name = random.choice(list(SHAPES.keys()))
    current_shape = list(SHAPES[name])
    current_color = COLORS[list(SHAPES.keys()).index(name)]
    current_x = COLS // 2 - 1
    current_y = 0
    
    if not is_valid_move(current_shape, current_x, current_y):
        print(f"Game Over! 최종 점수(지운 줄 수): {total_cleared_rows}")
        turtle.bye()

def is_valid_move(shape, offset_x, offset_y):
    """블록이 벽이나 고정된 다른 블록과 충돌하는지 검사합니다."""
    for dx, dy in shape:
        nx = offset_x + dx
        ny = offset_y + dy
        if nx < 0 or nx >= COLS or ny >= ROWS:
            return False
        if ny >= 0 and board[ny][nx] != 0:
            return False
    return True

def rotate_block():
    """블록을 시계 방향으로 90도 회전시킵니다."""
    global current_shape
    rotated = [(-y, x) for x, y in current_shape]
    if is_valid_move(rotated, current_x, current_y):
        current_shape = rotated
        draw_scene()

def move_left():
    global current_x
    if is_valid_move(current_shape, current_x - 1, current_y):
        current_x -= 1
        draw_scene()

def move_right():
    global current_x
    if is_valid_move(current_shape, current_x + 1, current_y):
        current_x += 1
        draw_scene()

def move_down():
    """방향키(Down): 블록을 수동으로 한 줄 아래로 내립니다."""
    global current_y
    if is_valid_move(current_shape, current_x, current_y + 1):
        current_y += 1
        draw_scene()

def hard_drop():
    """스페이스바(Space): 블록을 바닥까지 한번에 즉시 떨어뜨리고 화면을 바로 새로고침합니다."""
    global current_y
    # 충돌하기 직전 위치까지 최대한 y값 증가
    while is_valid_move(current_shape, current_x, current_y + 1):
        current_y += 1
    # 보드에 블록 고정 및 새 블록 생성 처리
    freeze_block()
    # 피드백 반영: 고정 및 교체된 상태를 타이머 대기 없이 '즉시' 화면에 렌더링
    draw_scene()

def freeze_block():
    """바닥이나 블록에 닿은 현재 블록을 보드에 고정합니다."""
    for dx, dy in current_shape:
        nx = current_x + dx
        ny = current_y + dy
        if 0 <= ny < ROWS and 0 <= nx < COLS:
            board[ny][nx] = current_color
    clear_rows()
    create_new_block()

def clear_rows():
    """꽉 찬 줄을 지우고 속도를 실시간으로 업데이트합니다."""
    global board, total_cleared_rows, current_speed
    
    new_board = [row for row in board if 0 in row]
    cleared = ROWS - len(new_board)
    
    if cleared > 0:
        board = [[0] * COLS for _ in range(cleared)] + new_board
        total_cleared_rows += cleared
        
        # 1줄 지울 때마다 타이머를 50ms씩 단축 (최소 200ms 한계 제한)
        current_speed = max(200, INIT_SPEED - (total_cleared_rows * 50))
        
        print(f"줄 제거! 총 지운 줄 수: {total_cleared_rows} | 현재 하강 속도 주기: {current_speed}ms")
        turtle.title(f"Mini Tetris | Lines: {total_cleared_rows} | Speed Level: {1050 - current_speed}")

def drop_block():
    """current_speed 주기에 맞춰 블록을 자동 하강시킵니다."""
    global current_y
    if is_valid_move(current_shape, current_x, current_y + 1):
        current_y += 1
    else:
        freeze_block()
    draw_scene()
    turtle.ontimer(drop_block, current_speed)

def draw_square(x, y, color):
    """주어진 좌표에 지정된 색상의 정사각형 격자를 그립니다."""
    screen_x = -100 + (x * PIXEL)
    screen_y = 200 - (y * PIXEL)
    
    drawer.penup()
    drawer.goto(screen_x, screen_y)
    drawer.color(color)
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(PIXEL - 1)
        drawer.right(90)
    drawer.end_fill()

def draw_scene():
    """전체 화면을 렌더링합니다."""
    drawer.clear()
    
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != 0:
                draw_square(c, r, board[r][c])
            else:
                draw_square(c, r, "gray")
                
    for dx, dy in current_shape:
        draw_square(current_x + dx, current_y + dy, current_color)
        
    turtle.update()

# --- 메인 시스템 초기화 및 실행 ---
turtle.setup(width=400, height=600)
turtle.title(f"Mini Tetris | Lines: 0 | Speed Level: {1050 - current_speed}")
turtle.bgcolor("black")
turtle.tracer(0)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

# 키보드 이벤트 바인딩 설정
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(rotate_block, "Up")
turtle.onkey(move_down, "Down")    
turtle.onkey(hard_drop, "space")   # 스페이스바 기능 바인딩

create_new_block()
drop_block()
turtle.mainloop()