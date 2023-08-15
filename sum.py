# test
'''
testestestest
'''
sum = 0 # sum of numbers
for i in range(1, 101):
    print(sum, "+", i, "=", end=" ")
    sum = sum + i
    print(sum)
print("\n> 1+2+3+...+100 =", sum)