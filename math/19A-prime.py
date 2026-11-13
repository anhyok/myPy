x = int(input("?"))
d = 2

while d <= x:
    if x % d == 0:
        print(d)
        x = x / d
    else:
        #d = d + 1 if d == 2 else d + 2
        d = d + 1
