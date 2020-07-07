t = int(input())
for z in range(t):
    a, b = input().split()
    c = 0
    A = [0]*26
    B = [0]*26
    for i in a:
        A[ord(i) - 97] += 1
    for i in b:
        B[ord(i) - 97] += 1
    for i in range(26):
        if A[i] > 0 and B[i] > 0:
            m = min(A[i], B[i])
            c += m
            A[i] -= m
            B[i] -= m
    print((len(a) - c) + (len(b) - c))
