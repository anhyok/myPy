ip = input("n = ? ")
n = int(ip)
print("=[1]=========")

#*
#**
#***
#****
#*****
for i in range(1, n + 1):
    print("*" * i)


print("=[2]=========")


for i in range(n, 0, -1):
    print("*" * i)


print("=[3]=========")

#     *
#    *
#   *
#  *
# *
for i in range(n, 0, -1):
    print(" " * i, "*")
    

print("=[4]=========")


#          *
#         **
#        ***
#       ****
#      *****
      
for i in range(n, 0, -1):
    print(" " * i, "*" * (n-i+1))
      

print("=[5]=========")


#     *
#    ***
#   *****
#  *******
      
for i in range(n, 0, -1):
    print(" " * i, "*" * (2 * (n-i+1) - 1))
      
