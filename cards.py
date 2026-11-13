def solution(cards1, cards2, goal):
    while goal and (cards1 or cards2):
        if cards1 and cards1[0] == goal[0]:
            del cards1[0]
            del goal[0]
            continue
        elif cards2 and cards2[0] == goal[0]:
            del cards2[0]
            del goal[0]
            continue
        return "No"     
    return "Yes"

solution(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["string", "or", "integer"], ["string", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
