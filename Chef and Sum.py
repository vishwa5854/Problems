T = int(input())
for z in range(T):
    N, K = map(int, input().split())
    lol = list(map(int, input().split()))
    ans = "No"
    for i in range(N):
        for j in range(i+1, N):
            if lol[i] + lol[j] == K:
                ans = "Yes"
                break
    print(ans)
