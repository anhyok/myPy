# 분수의 덧셈
def solution(numer1, denom1, numer2, denom2):
    answer = []
    # hint 1: a/b + c/d = (a*d + c*b) / b*d
    # 분자: a*d + c*b
    numer_new = numer1 * denom2 + numer2 * denom1
    # 분모: b*d
    denom_new = denom1 * denom2
    #약분
    # hint 2: 기약 분수 즉, 약분할 것 ==> 2/4 = 1/2
    i = 2
    # 6/15의 경우 7로 나눠볼 필요가 있을까?
    while i <= numer_new or i <= denom_new:
        # 2로 나눠보고, 3으로 나눠보고, .......
        # 나누어 떨어진다 = 약분가능
        if (numer_new % i == 0) and (denom_new % i == 0):
            numer_new = numer_new // i
            denom_new = denom_new // i
        else:
            i = i+ 1
    answer = [numer_new, denom_new]
    return answer



print(solution(1,2,3,4))
print(solution(9,2,1,3))
