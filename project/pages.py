def pages(n):
    if n % 10 == 0:
        page = n // 10
    else:   
        page = n // 10 + 1
    return page

print(pages(15))
print(pages(25))
print(pages(30))
