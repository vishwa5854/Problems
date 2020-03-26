T = int(input())
for z in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = False
    for i in arr:
        if K - i in arr:
            ans = True
            break
    print(ans)
