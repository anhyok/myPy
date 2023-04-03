def lcm(a, b):
    for x in range(max(a, b), a*b+1):
        if (x % a == 0) and (x % b == 0):
            return x
    
def solution(n): 
    answer = lcm(n, 6) // 6
    return answer

print(solution(6))
print(solution(10))
print(solution(4))
