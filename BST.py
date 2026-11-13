from bst_visualizer import BSTVisualizer

# ==========================================
# 1. 노드 클래스 정의
# ==========================================
class BSTNode:
    def __init__(self, key, value):
        self.key = key          # 키(key)
        self.value = value      # 값(value)
        self.left = None        # 왼쪽 자식 링크
        self.right = None       # 오른쪽 자식 링크

    def __str__(self):
        return f"({self.key}:{self.value})"


# ==========================================
# 2. 탐색 및 삽입 함수
# ==========================================
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)

def insert_bst(root, node):
    if root == None:
        return node
    
    if node.key == root.key:
        return root
    
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
        
    return root


# ==========================================
# 3. 노드 삭제 함수 (delete_bst)
# ==========================================
def delete_bst(root, key):
    if root == None:  # 공백 트리
        return root

    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        # case 1(단말 노드) 또는 case 2(오른쪽 자식만 있는 경우)
        if root.left == None:
            return root.right

        # case 2(왼쪽 자식만 있는 경우)
        if root.right == None:
            return root.left

        # case 3(두 자식이 모두 있는 경우)
        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)

    return root


# ==========================================
# 4. 출력 및 테스트용 보조 함수 (실행 결과 형식 반영)
# ==========================================
def preorder(n):
    """전위 순회 함수: 서브트리를 중괄호({})로 묶어 출력"""
    if n is not None:
        print('{', end='')
        print(n, end='')
        preorder(n.left)
        preorder(n.right)
        print('}', end='')

def print_node(msg, n):
    """노드 출력 함수"""
    print(msg, n if n != None else "탐색실패")

def print_tree(msg, r):
    """전위 순회를 이용한 트리 출력 함수"""
    print(msg, end='')
    preorder(r)
    print()
    BSTVisualizer.show(msg, r)  # GUI 창으로 현재 트리 시각화


# ==========================================
# 5. 실행 및 테스트 코드
# ==========================================
if __name__ == "__main__":
    data = [
        (6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"),
        (5, "다섯"), (1, "하나"), (9, "아홉"), (3, "셋"), (0, "영")
    ]

    root = None
    for i in range(0, len(data)):
        root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

    print_tree("최초: ", root)

    # key를 이용한 탐색
    n = search_bst(root, 3);  print_node("srch 3: ", n)
    n = search_bst(root, 8);  print_node("srch 8: ", n)
    n = search_bst(root, 0);  print_node("srch 0: ", n)
    n = search_bst(root, 10); print_node("srch10: ", n)

    # 값(value)을 이용한 탐색
    n = search_value_bst(root, "둘"); print_node("srch둘: ", n)
    n = search_value_bst(root, "열"); print_node("srch열: ", n)

    # 노드 삭제 테스트
    root = delete_bst(root, 7); print_tree("del  7: ", root)
    root = delete_bst(root, 8); print_tree("del  8: ", root)
    root = delete_bst(root, 2); print_tree("del  2: ", root)
    root = delete_bst(root, 6); print_tree("del  6: ", root)


print("===========================================")
print("BST 탐색 및 삽입 테스트")
print("===========================================")

BSTroot = None

# 노드 삽입 테스트
data = [(35, '선풍기'), (18, '달력'), (68, '시계'), (7, '에어컨'), (26, '세탁기')]
for key, value in data:
    BSTroot = insert_bst(BSTroot, BSTNode(key, value))

# 키 탐색 테스트
target_node = search_bst(BSTroot, 18)
if target_node:
    print(f"키 18 탐색 성공: {target_node.value}")
else:
    print("키 18 탐색 실패")
target_node = search_bst(BSTroot, 19)
if target_node:
    print(f"키 19 탐색 성공: {target_node.value}")
else:
    print("키 19 탐색 실패")

# 값 탐색 테스트
target_node_val = search_value_bst(BSTroot, '에어컨')
if target_node_val:
    print(f"값 '에어컨' 탐색 성공: 키={target_node_val.key}")
else:
    print("값 '에어컨' 탐색 실패")
target_node_val = search_value_bst(BSTroot, 'TV')
if target_node_val:
    print(f"값 'TV' 탐색 성공: 키={target_node_val.key}")
else:
    print("값 'TV' 탐색 실패")