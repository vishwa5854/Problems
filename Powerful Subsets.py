from math import log2

T = int(input())
for z in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = "NO"
    for i in range(1 << N):
        s = 2147483647
        for j in range(N):
            if (i & (1 << j)) > 0:
                s = s & arr[j]
        if s != 2147483647:
            if s != 0:
                if log2(s).is_integer():
                    ans = "YES"
                    break
    print(ans)
