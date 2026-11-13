def collatz(cnt, num):
    #print(cnt, num)
    if cnt == 500:
        return -1
    elif num == 1:
        return cnt
    elif num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    cnt += 1
    
    return collatz(cnt, num)

def solution(num):
    return collatz(0, num)

print(solution(6))
