y = [10, 20, 30]

try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except Exception as e:
    print('예외가 발생했습니다.')
except ZeroDivisionError as e:
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError as e:
    print('잘못된 인덱스입니다.')