import tkinter as tk
from tkinter import messagebox


class BSTVisualizer:
    @staticmethod
    def _assign_positions(node, depth, counter, positions):
        """중위 순회 순서를 이용해 노드가 겹치지 않도록 가로(slot)·세로(depth) 좌표 배정"""
        if node is None:
            return
        BSTVisualizer._assign_positions(node.left, depth + 1, counter, positions)
        positions[node] = (counter[0], depth)
        counter[0] += 1
        BSTVisualizer._assign_positions(node.right, depth + 1, counter, positions)

    @classmethod
    def draw_on_canvas(cls, canvas, root_node, highlight_node=None):
        """전달받은 Canvas 위에 트리를 렌더링"""
        canvas.delete("all")
        if root_node is None:
            canvas.create_text(
                max(canvas.winfo_width(), 600) // 2,
                max(canvas.winfo_height(), 400) // 2,
                text="공백 트리 (Empty Tree)",
                fill="gray",
                font=("", 13),
            )
            return

        positions = {}
        counter = [0]
        cls._assign_positions(root_node, 0, counter, positions)

        total_nodes = counter[0]
        max_depth = max(depth for _, depth in positions.values())

        width = max(canvas.winfo_width(), 720)
        height = max(canvas.winfo_height(), 440)
        margin_x = 60
        margin_y = 55
        radius = 26

        x_step = (width - 2 * margin_x) / max(total_nodes - 1, 1)
        y_step = min(85, (height - 2 * margin_y) / max(max_depth, 1))

        pixel_coords = {}
        for node, (slot, depth) in positions.items():
            px = width / 2 if total_nodes == 1 else margin_x + slot * x_step
            py = margin_y + depth * y_step
            pixel_coords[node] = (px, py)

        # 부모-자식 연결선 그리기
        for node, (px, py) in pixel_coords.items():
            if node.left is not None:
                cx, cy = pixel_coords[node.left]
                canvas.create_line(px, py, cx, cy, width=2, fill="#607D8B")
            if node.right is not None:
                cx, cy = pixel_coords[node.right]
                canvas.create_line(px, py, cx, cy, width=2, fill="#607D8B")

        # 노드 원형 및 (key / value) 텍스트 그리기
        for node, (px, py) in pixel_coords.items():
            is_target = (node == highlight_node)
            fill_color = "#FFE082" if is_target else "#E8F5E9"
            outline_color = "#F57C00" if is_target else "#2E7D32"
            outline_width = 3 if is_target else 2

            canvas.create_oval(
                px - radius, py - radius, px + radius, py + radius,
                fill=fill_color, outline=outline_color, width=outline_width,
            )
            canvas.create_text(
                px, py,
                text=f"{node.key}\n({node.value})",
                font=("", 9, "bold"),
                fill="#212121",
                justify=tk.CENTER,
            )

    @classmethod
    def show(cls, msg, root_node):
        """print_tree(msg, r) 내부에서 호출하여 현재 트리 상태를 GUI 창으로 표시"""
        win = tk.Tk()
        win.title(f"BST 출력 - {msg.strip()}")
        win.geometry("760x500")

        top_frame = tk.Frame(win, pady=8)
        top_frame.pack(fill=tk.X)

        tk.Label(
            top_frame, text=f"상태: {msg.strip()}", fg="#1565C0", font=("", 11, "bold")
        ).pack(side=tk.LEFT, padx=15)

        tk.Button(
            top_frame, text="다음 단계 진행 (창 닫기)", bg="#E3F2FD", command=win.destroy
        ).pack(side=tk.RIGHT, padx=15)

        canvas = tk.Canvas(win, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        canvas.bind("<Configure>", lambda e: cls.draw_on_canvas(canvas, root_node))

        win.update_idletasks()
        cls.draw_on_canvas(canvas, root_node)
        win.mainloop()

    @classmethod
    def interactive(cls, root_node, node_cls, insert_fn, delete_fn, search_fn, search_val_fn):
        """기존 BST 함수들을 주입받아 삽입·삭제·탐색을 직접 조작하는 대화형 GUI 실행"""
        win = tk.Tk()
        win.title("이진 탐색 트리(BST) 대화형 시각화")
        win.geometry("900x580")

        state = {"root": root_node, "highlight": None}

        ctrl = tk.Frame(win, pady=10)
        ctrl.pack(fill=tk.X)

        tk.Label(ctrl, text="Key:").pack(side=tk.LEFT, padx=(15, 3))
        key_entry = tk.Entry(ctrl, width=8)
        key_entry.pack(side=tk.LEFT, padx=3)

        tk.Label(ctrl, text="Value:").pack(side=tk.LEFT, padx=(10, 3))
        val_entry = tk.Entry(ctrl, width=10)
        val_entry.pack(side=tk.LEFT, padx=3)

        status_var = tk.StringVar(value="트리가 로드되었습니다. 삽입/삭제/탐색을 실행해 보세요.")

        def refresh():
            cls.draw_on_canvas(canvas, state["root"], state["highlight"])

        def handle_insert():
            try:
                k = int(key_entry.get().strip())
            except ValueError:
                messagebox.showwarning("입력 오류", "Key는 정수로 입력하세요.")
                return
            v = val_entry.get().strip() or str(k)
            state["root"] = insert_fn(state["root"], node_cls(k, v))
            state["highlight"] = search_fn(state["root"], k)
            status_var.set(f"삽입 완료: ({k}:{v})")
            refresh()

        def handle_delete():
            try:
                k = int(key_entry.get().strip())
            except ValueError:
                messagebox.showwarning("입력 오류", "삭제할 Key를 정수로 입력하세요.")
                return
            state["highlight"] = None
            state["root"] = delete_fn(state["root"], k)
            status_var.set(f"del {k}: 키 {k} 삭제 수행")
            refresh()

        def handle_search_key():
            try:
                k = int(key_entry.get().strip())
            except ValueError:
                messagebox.showwarning("입력 오류", "탐색할 Key를 정수로 입력하세요.")
                return
            found = search_fn(state["root"], k)
            state["highlight"] = found
            status_var.set(f"srch {k}: {found if found else '탐색실패'}")
            refresh()

        def handle_search_val():
            v = val_entry.get().strip()
            if not v:
                messagebox.showwarning("입력 오류", "탐색할 Value를 입력하세요.")
                return
            found = search_val_fn(state["root"], v)
            state["highlight"] = found
            status_var.set(f"srch '{v}': {found if found else '탐색실패'}")
            refresh()

        tk.Button(ctrl, text="삽입", width=7, command=handle_insert).pack(side=tk.LEFT, padx=4)
        tk.Button(ctrl, text="삭제", width=7, command=handle_delete).pack(side=tk.LEFT, padx=4)
        tk.Button(ctrl, text="Key 탐색", width=9, command=handle_search_key).pack(side=tk.LEFT, padx=4)
        tk.Button(ctrl, text="Value 탐색", width=10, command=handle_search_val).pack(side=tk.LEFT, padx=4)

        tk.Label(win, textvariable=status_var, fg="#1565C0", font=("", 10, "bold")).pack(pady=2)

        canvas = tk.Canvas(win, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        canvas.pack(fill=tk.BOTH, expand=True, padx=15, pady=(5, 15))
        canvas.bind("<Configure>", lambda e: refresh())

        win.update_idletasks()
        refresh()
        win.mainloop()


# ==========================================
# 단독 실행 시 동작하는 모듈 테스트용 메인 함수
# ==========================================
if __name__ == "__main__":
    class _TestNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return f"({self.key}:{self.value})"

    def _test_insert(root, node):
        if root is None:
            return node
        if node.key < root.key:
            root.left = _test_insert(root.left, node)
        elif node.key > root.key:
            root.right = _test_insert(root.right, node)
        return root

    def _test_delete(root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = _test_delete(root.left, key)
        elif key > root.key:
            root.right = _test_delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ = root.right
            while succ.left is not None:
                succ = succ.left
            root.key, root.value = succ.key, succ.value
            root.right = _test_delete(root.right, succ.key)
        return root

    def _test_search(n, key):
        if n is None or n.key == key:
            return n
        return _test_search(n.left, key) if key < n.key else _test_search(n.right, key)

    def _test_search_val(n, value):
        if n is None or n.value == value:
            return n
        res = _test_search_val(n.left, value)
        return res if res is not None else _test_search_val(n.right, value)

    # 샘플 데이터로 초기 트리 생성
    sample_data = [
        (6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"),
        (5, "다섯"), (1, "하나"), (9, "아홉"), (3, "셋"), (0, "영")
    ]
    test_root = None
    for k, v in sample_data:
        test_root = _test_insert(test_root, _TestNode(k, v))

    # 1) 정적 출력 창(show) 테스트
    BSTVisualizer.show("단독 테스트 - 초기 트리", test_root)

    # 2) 대화형 GUI(interactive) 테스트
    BSTVisualizer.interactive(
        test_root, _TestNode, _test_insert, _test_delete, _test_search, _test_search_val
    )