n = int(input())
for i in range(n):
    a = int(input())
    b = list(map(int, input().split()))
    for j in b:
        t = 0
        if t > j:
            index = b.index(i)
            print(index)
        t += 1
