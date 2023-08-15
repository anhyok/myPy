#문제: https://school.programmers.co.kr/learn/courses/30/lessons/120815
#최소공배수(lcm)
def lcm(a, b):
    #최소공배수 x는 a 또는 b보다 작을 수 없다
    #최소공배수 x는 a * b보다 클 수 없다
    #그러므로, max(a,b) <= x <= a*b
    for x in range(max(a, b), a*b+1): #a,b 중 큰 수부터 a*b까지 순서대로 나눠보자
    #for x in range(1, a*b+1): #1부터 시작해도 작동한다.
    #for x in range(0, a*b+1): #0부터 시작하면 안된다. 0은 나눌 수 없다.
        if (x % a == 0) and (x % b == 0): #a와 b로 나눌 수 있는 첫번째 수 x
            return x # x는 제일 작은 a, b의 배수 = 최소공배수
    
def solution(n): 
    answer = lcm(n, 6) // 6 #피자 수 = 피자조각 수 / 6
    return answer


#이하, 작동 확인용 코드
print(solution(6))
print(solution(10))
print(solution(4))
