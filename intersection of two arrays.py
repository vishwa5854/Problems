T = int(input())
for z in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = set()
    D = set()
    ans = 0
    for i in A:
        C.add(i)
    for i in B:
        D.add(i)
    for i in D:
        if i in C:
            ans += 1
    print(ans)
