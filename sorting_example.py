# Example: https://school.programmers.co.kr/learn/courses/30/lessons/120850

### 선택정렬(쉬움)
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort_simple(a):
    result = []
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

### 선택정렬(일반)
def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

### 삽입정렬(쉬움)
def find_ins_idx(r, v):
    for i in range(0, len(r)):
        if v < r[i]:
            return i
    return len(r)

def ins_sort_simple(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        #print(a, result)
    return result

### 삽입정렬(일반)
def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key

### 병합정렬(쉬움)
def merge_sort_simple(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    g1 = merge_sort_simple(a[:mid])
    g2 = merge_sort_simple(a[mid:])
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

### 병합정렬(일반)
def merge_sort(a):
    n = len(a)
    if n <= 1:
        return
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]
    merge_sort(g1)
    merge_sort(g2)
    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = g2[i2]
            i2 += 1
            ia += 1
    while i1 < len(g1):
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2):
        a[ia] = g2[i2]
        i2 += 1
        ia += 1
    
def solution(my_string):
    answer = []
    for x in my_string:
        if x.isdecimal(): # int()로 변경가능한 숫자? (변환 가능여부까지 판별해주기 때문에 isdigit()보다 적절함)
            answer.append(int(x)) # add a number to the 'answer' list : unsorted yet.

    # Let's sort!
    answer = sel_sort_simple(answer)    ### 선택정렬(쉬움)
    #sel_sort(answer)                   ### 선택정렬(일반) 
    #answer = ins_sort_simple(answer)   ### 삽입정렬(쉬움)
    #ins_sort(answer)                   ### 삽입정렬(일반)
    #answer = merge_sort_simple(answer) ### 병합정렬(쉬움)
    #merge_sort(answer)                 ### 병합정렬(일반)
        
    return answer


##########
# 실행용 코드 (programmers.co.kr에서 실행 시 필요 없음)
print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))