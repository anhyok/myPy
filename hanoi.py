def hanoi(n, start, mid, end):
    if n == 0:
        return

    hanoi(n-1, start, end, mid)
    print(n, ": ", start, "->", end)
    hanoi(n-1, mid, start, end)

hanoi(3, 'A', 'B', 'C')
