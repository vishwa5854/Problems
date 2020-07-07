T = int(input())
for z in range(T):
    N, A, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if A <= sum(arr[i: j + 1]) <= B:
                ans += 1
    print(ans)
