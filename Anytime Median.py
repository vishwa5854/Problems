import heapq

T = int(input())
for z in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    a = []
    heapq.heapify(a)
    for i in range(N):
        heapq.heappush(a, arr[i])
        pr