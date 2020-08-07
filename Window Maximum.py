import heapq

T = int(input())
for z in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    b = {}
    for i in range(N):
        b[arr[i]] = i
    ans = 0
    a = []
    heapq.heapify(a)
    for i in range(K):
        heapq.heappush(a, -arr[i])
    temp = -heapq.heappop(a)
    ans += temp
    if b[temp] >= K - i - 1:
        heapq.heappush(a, -temp)
    # print(temp, end=" ")
    for i in range(N - K):
        heapq.heappush(a, -arr[K + i])
        temp = -heapq.heappop(a)
        ans += temp
        # print(temp, end=" ")
        if b[temp] >= i + K - 1:
            heapq.heappush(a, -temp)
    print(ans)
