import tkinter as tk
from tkinter import messagebox, simpledialog
import socket
import threading
import json
import random

# 게임 설정 변수
ROW, COL = 20, 10
BLOCK_SIZE = 25

# 테트로미노 모양 정의 (I, J, L, O, S, T, Z)
SHAPES = [
    [[1, 1, 1, 1]], # I
    [[1, 0, 0], [1, 1, 1]], # J
    [[0, 0, 1], [1, 1, 1]], # L
    [[1, 1], [1, 1]], # O
    [[0, 1, 1], [1, 1, 0]], # S
    [[0, 1, 0], [1, 1, 1]], # T
    [[1, 1, 0], [0, 1, 1]]  # Z
]

COLORS = ["cyan", "blue", "orange", "yellow", "green", "purple", "red"]

class NetworkTetris:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("테트리스 2인 배틀 모드 (LAN 대전)")
        
        # 1. 게임 접속 모드 선택
        self.mode = simpledialog.askstring("모드 선택", "'server' 또는 'client'를 입력하세요:", parent=self.root)
        if self.mode not in ['server', 'client']:
            messagebox.showerror("오류", "올바른 모드를 입력하지 않아 종료합니다.")
            self.root.destroy()
            return
            
        self.root.title(f"테트리스 대전 - [{self.mode.upper()} 화면]")

        # 2. GUI 레이아웃 설정
        my_frame = tk.Frame(self.root)
        my_frame.pack(side=tk.LEFT, padx=15, pady=15)
        tk.Label(my_frame, text="내 화면 (PLAYER)", font=("Arial", 12, "bold")).pack()
        self.my_canvas = tk.Canvas(my_frame, width=COL*BLOCK_SIZE, height=ROW*BLOCK_SIZE, bg='black')
        self.my_canvas.pack()

        # 상대방 게임판
        opp_frame = tk.Frame(self.root)
        opp_frame.pack(side=tk.RIGHT, padx=15, pady=15)
        tk.Label(opp_frame, text="상대방 화면 (OPPONENT)", font=("Arial", 12, "bold")).pack()
        self.opp_canvas = tk.Canvas(opp_frame, width=COL*BLOCK_SIZE, height=ROW*BLOCK_SIZE, bg='#222222')
        self.opp_canvas.pack()

        # 3. 게임 내부 데이터 초기화
        self.my_board = [[0] * COL for _ in range(ROW)]
        self.current_piece = None
        self.current_color = ""
        self.px, self.py = 0, 0
        self.game_over = False
        
        # 4. 네트워크 소켓 및 스레드 설정
        self.conn = None
        self.setup_network()
        
        # 5. 키 바인딩 및 게임 시작
        if not self.game_over:
            self.root.bind("<Key>", self.handle_key)
            self.new_block()
            self.auto_drop()
            
        self.root.mainloop()

    def setup_network(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # 대전에서 사용할 고정 포트 번호
        port = 9999
        
        if self.mode == "server":
            # 3단계 수정: 127.0.0.1 대신 0.0.0.0을 사용하여 외부 PC의 접속을 허용합니다.
            sock.bind(("0.0.0.0", port))
            sock.listen(1)
            print("상대방의 접속을 기다리는 중입니다... (IP주소를 상대방에게 알려주세요)")
            self.conn, addr = sock.accept()
            print(f"상대방 연결 성공: {addr}")
        else:
            # 3단계 추가: 클라이언트 모드일 때 서버(방장)의 IP를 직접 입력받습니다.
            server_ip = simpledialog.askstring("IP 입력", "서버(방장)의 IP 주소를 입력하세요:", parent=self.root)
            if not server_ip:
                self.game_over = True
                self.root.destroy()
                return
            try:
                sock.connect((server_ip, port))
                self.conn = sock
                print("서버에 성공적으로 연결되었습니다!")
            except Exception as e:
                messagebox.showerror("연결 실패", f"서버({server_ip})에 연결할 수 없습니다.\nIP주소나 방화벽 설정을 확인하세요.")
                self.game_over = True
                self.root.destroy()
                return

        threading.Thread(target=self.receive_thread, daemon=True).start()

    def send_packet(self, data_dict):
        if not self.conn or self.game_over:
            return
        try:
            packet = json.dumps(data_dict) + "\n"
            self.conn.sendall(packet.encode('utf-8'))
        except Exception as e:
            print("데이터 전송 오류:", e)

    def send_my_state(self):
        state_data = {
            "type": "sync",
            "board": self.my_board,
            "piece": self.current_piece,
            "px": self.px,
            "py": self.py,
            "color": self.current_color
        }
        self.send_packet(state_data)

    def receive_thread(self):
        buffer = ""
        while True:
            try:
                data = self.conn.recv(4096)
                if not data: break
                
                buffer += data.decode('utf-8')
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    msg = json.loads(line)
                    
                    if msg["type"] == "sync":
                        self.draw_opponent_board(msg)
                    elif msg["type"] == "attack":
                        self.receive_attack(msg["lines"])
            except Exception as e:
                print("데이터 수신 오류:", e)
                break

    # --- 테트리스 핵심 및 추가 기능 로직 ---
    def new_block(self):
        idx = random.randint(0, len(SHAPES) - 1)
        self.current_piece = SHAPES[idx]
        self.current_color = COLORS[idx]
        self.px = COL // 2 - len(self.current_piece[0]) // 2
        self.py = 0
        
        if self.check_collision(self.current_piece, self.px, self.py):
            self.game_over = True
            messagebox.showinfo("Game Over", "게임에서 패배했습니다!")
            
        self.draw_my_scene()
        self.send_my_state()

    def check_collision(self, piece, nx, ny):
        for r in range(len(piece)):
            for c in range(len(piece[r])):
                if piece[r][c] != 0:
                    if nx + c < 0 or nx + c >= COL or ny + r >= ROW:
                        return True
                    if self.my_board[ny + r][nx + c] != 0:
                        return True
        return False

    def merge_block(self):
        for r in range(len(self.current_piece)):
            for c in range(len(self.current_piece[r])):
                if self.current_piece[r][c] != 0:
                    self.my_board[self.py + r][self.px + c] = self.current_color

        full_lines_count = 0
        for r in range(ROW):
            if all(self.my_board[r][c] != 0 for c in range(COL)):
                full_lines_count += 1

        if full_lines_count > 0:
            attack_packet = {
                "type": "attack",
                "lines": full_lines_count
            }
            self.send_packet(attack_packet)

        self.clear_lines()
        self.new_block()

    def clear_lines(self):
        new_board = [row for row in self.my_board if any(val == 0 for val in row)]
        cleared = ROW - len(new_board)
        if cleared > 0:
            for _ in range(cleared):
                new_board.insert(0, [0] * COL)
            self.my_board = new_board

    def receive_attack(self, lines_count):
        self.my_board = self.my_board[lines_count:]
        for _ in range(lines_count):
            empty_col = random.randint(0, COL - 1)
            new_row = ["gray" if c != empty_col else 0 for c in range(COL)]
            self.my_board.append(new_row)
            
        self.draw_my_scene()
        self.send_my_state()

    def rotate_block(self):
        rotated = list(zip(*self.current_piece[::-1]))
        rotated = [list(row) for row in rotated]
        if not self.check_collision(rotated, self.px, self.py):
            self.current_piece = rotated
            self.draw_my_scene()
            self.send_my_state()

    def move_block(self, dx, dy):
        if not self.check_collision(self.current_piece, self.px + dx, self.py + dy):
            self.px += dx
            self.py += dy
            self.draw_my_scene()
            self.send_my_state()
            return True
        elif dy > 0:
            self.merge_block()
            return False

    def hard_drop(self):
        while self.move_block(0, 1):
            pass

    def auto_drop(self):
        if not self.game_over:
            self.move_block(0, 1)
            self.root.after(500, self.auto_drop)

    def handle_key(self, event):
        if self.game_over: return
        if event.keysym == "Left":   self.move_block(-1, 0)
        elif event.keysym == "Right": self.move_block(1, 0)
        elif event.keysym == "Down":  self.move_block(0, 1)
        elif event.keysym == "Up":    self.rotate_block()
        elif event.keysym == "space": self.hard_drop()

    # --- 그래픽 렌더링 함수 ---
    def draw_my_scene(self):
        self.my_canvas.delete("all")
        for r in range(ROW):
            for c in range(COL):
                if self.my_board[r][c] != 0:
                    self.my_canvas.create_rectangle(c*BLOCK_SIZE, r*BLOCK_SIZE, (c+1)*BLOCK_SIZE, (r+1)*BLOCK_SIZE, fill=self.my_board[r][c], outline="white")
                    
        if self.current_piece:
            for r in range(len(self.current_piece)):
                for c in range(len(self.current_piece[r])):
                    if self.current_piece[r][c] != 0:
                        self.my_canvas.create_rectangle((self.px+c)*BLOCK_SIZE, (self.py+r)*BLOCK_SIZE, (self.px+c+1)*BLOCK_SIZE, (self.py+r+1)*BLOCK_SIZE, fill=self.current_color, outline="white")

    def draw_opponent_board(self, opp_state):
        self.opp_canvas.delete("all")
        opp_board = opp_state["board"]
        opp_piece = opp_state["piece"]
        opx, opy = opp_state["px"], opp_state["py"]
        color = opp_state["color"]

        for r in range(ROW):
            for c in range(COL):
                if opp_board[r][c] != 0:
                    self.opp_canvas.create_rectangle(c*BLOCK_SIZE, r*BLOCK_SIZE, (c+1)*BLOCK_SIZE, (r+1)*BLOCK_SIZE, fill=opp_board[r][c], outline="gray")

        if opp_piece:
            for r in range(len(opp_piece)):
                for c in range(len(opp_piece[r])):
                    if opp_piece[r][c] != 0:
                        self.opp_canvas.create_rectangle((opx+c)*BLOCK_SIZE, (opy+r)*BLOCK_SIZE, (opx+c+1)*BLOCK_SIZE, (opy+r+1)*BLOCK_SIZE, fill=color, outline="gray")

if __name__ == "__main__":
    NetworkTetris()