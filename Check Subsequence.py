t = int(input())
for z in range(t):
    a, b = input().split()
    A = [False] * len(a)
    c = 0
    start = 0
    for i in a:
        for j in range(start, len(b)):
            if i == b[j]:
                start = j
                A[c] = True
                c += 1
                break
    v = 0
    for i in A:
        if i:
            v += 1
    if v == len(a):
        print("Yes")
    else:
        print("No")
