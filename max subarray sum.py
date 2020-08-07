T = int(input())
for z in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    interval = [[]]
    ans = 0
    start0 = 0
    end0 = 0
    temp = 0
    for i in range(N):
        temp += arr[i]
        if temp < 0:
            temp = 0
            start0 = i + 1
        ans = max(ans, temp)
        if temp >= ans:
            end0 = i
    print(ans, start0, end0)
