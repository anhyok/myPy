import random
import time

w = ["cat", "dog", "fox", "monky",
     "mouse", "panda", "frog",
     "snake", "worf"]
n = 1
print("Ready? [Enter]")
input()
start = time.time()
q = random.choice(w)
while n <= 5:
    print("*Q:", n)
    print(q)
    x = input()
    if q == x:
        print("Pass!")
        n = n + 1
        q = random.choice(w)
    else:
        print("Wrong! Retry")

end = time.time()
et = end - start
et = format(et, ".2f")
print("Record: ", et, "s")
