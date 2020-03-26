def SUM(D, N):
    if D == 1:
        return int(N * (N + 1) / 2)
    return SUM(D - 1, N * (N + 1) / 2)


T = int(input())
for z in range(T):
    d, n = map(int, input().split())
    print(SUM(d, n))

