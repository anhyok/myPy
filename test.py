# n = 5
# for i in range(n):
#     print(" "*(n-i) + "*"*(i*2-1))
# for i in range(n, 0, -1):
#     print(" "*(n-i) + "*"*(i*2-1))

# for i in range(10, 0, -1):
#     if i % 2 == 1:
#         print(" "*(i//2), "*"*(10-i))
# for i in range(2,10):
#     if i%2 == 1:
#         print(" "*(i//2), "*"*(10-i))

# for i in range(1, 11, 2):
#     print("{0:^11}".format("*"*i))
# for i in range(11, 0, -2):
#     print("{0:^11}".format("*"*i))

# for i in range(5,0,-1):
#     print(" "*i, "*"*(2*(5-i+1)-1))
# for i in range(2, 5+1):
#     print(" "*i, "*"*(2*(5-i+1)-1))

# for i in range(1, 11, 2):
#     print("{0:^10}".format("*"*i))
# for i in range(9, 0, -2):
#     print("{0:^10}".format("*"*i))

# for x in range(1,6):
#     print(" "*(5-x), "*"*x, end="")
#     print("*"*(x-1))
# for x in range(5,0,-1):
#     print(" "*(5-x), "*"*x, end="")
#     print("*"*(x-1))

# for i in range(1,10,2):
#     print((" "*((9-i)//2)) + ("*"*i) + (" "*((9-i)//2)))
# for i in range(7,0,-2): 
#     print((" "*((9-i)//2)) + ("*"*i) + (" "*((9-i)//2)))

# for i in range(5):
#     print(("*"*(i+1)).rjust(5))

# for i in range(1,10):
#     if i <= 5:
#         for j in range(5-i):
#             print(" ", end="")
#         for j in range(2*i-1):
#             print("*", end="")
#         print()
#     else:
#         for j in range(i-5):
#             print(" ", end="")
#         for j in range((10-i)*2-1):
#             print("*", end="")
#         print()

# for i in range(0,5):
#     i = i+1
#     print('*' * (2*i-1))
# for i in range(6,10):
#     i = i-1
#     print('*' * (17-2*i))

# for x in range(9):
#     print(" "*(9-x) + "*"*x + "*"*(x-1) + " "*(9-x))
# for y in range(9):
#     print(" "*y + "*"*(9-y) + "*"*(8-y))# + " "*y)

# for x in range(5):
#     print(" "*(5-x) + "*"*(x*2-1))
# for y in range(5):
#     print(" "*y + "*"*(9-(2*y)))

# for x in range(1, 10):
#     if x%2 == 1:
#         y = 9-x
#         k=y//2
#         print(' '*k, '*'*x)
# for x in range(7,0,-1):
#     if x%2 == 1:
#         y = 9-x
#         k=y//2
#         print(' '*k, '*'*x)

# for i in range(0,5):
#     # print(" "*(5-i) + "*"*(i*2)+1)
#     print(" "*(5-i) + "*"*((i*2)+1))
# for j in range(4,0,-1):
#     # print(" "*(6-j) + "*"*(j*2)-1)
#     print(" "*(6-j) + "*"*((j*2)-1))

# for i in range(1, 10):
#     if i <= 5:
#         space = " " * (5-i)
#         star = "*" * (2*i-1)
#     else:
#         space = " " * (i -5)
#         star = "*" * (2*(10-i)-1)
#     result = f"{space}{star}"
#     print(result)

for b in range(5):
    print(" "*(5-b) + "*"*b + "*"*(b-1))
for c in range(5):
    print(" "*c + "*"*(5-c) + "*"*(4-c))