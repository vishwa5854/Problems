n = 1000
for i in range(4, n):
    a = 1
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            a -= 1
    if a == 1:
        print(i)
