############
# 3번 문제 #
############

def solution (n, lost, reserve) :
    print("n=", n, "lost=", lost, "reserve=", reserve)

    # 이곳에 코드 작성

    return -1


print("O") if solution(5, [2,4], [3]) == 4 else print("X")
print("O") if solution(3, [3], [1]) == 2 else print("X")
print("O") if solution(5, [4, 5], [3, 4]) == 4 else print("X")
print("O") if solution(5, [4, 2], [1, 3]) == 5 else print("X")
print("O") if solution(5, [4, 2], [3, 5]) == 5 else print("X")

