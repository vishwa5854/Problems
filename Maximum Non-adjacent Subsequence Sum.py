T = int(input())
for z in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0], arr[1]]
    for i in range(2, N):
        dp.append(max(dp[: i - 2 + 1]) + arr[i])
    print(dp[len(dp) - 1])
