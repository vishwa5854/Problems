# lol1 = list(range(50000))
# lol2 = list(range(50000))
# lol = lol1 + lol2
# N = 100000
# for i in range(N):
#     for j in range(i + 1, N):
#         if lol[i] + lol[j] == lol[i] * lol[j]:
#             print(lol[i], lol[j])

T = int(input())
for z in range(T):
    N = int(input())
    c = 0
    c1 = 0
    lol = list(map(int, input().split()))
    for i in lol:
        if i == 2:
            c1 += 1
        if i == 0:
            c += 1
    c3 = 0
    if c1 == 2:
        c3 += 1
    if c == 2:
        c3 += 1
    print(c3)
