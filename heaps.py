import heapq

heap = []
heapq.heapify(heap)
t = int(input())
while t:
    t -= 1
    arr = list(map(str, input().split()))
    if arr[0] == "insert":
        heapq.heappush(heap, int(arr[1]))
    elif arr[0] == "getMin":
        if len(heap) == 0:
            print('Empty')
        else:
            print(heap[0])
    else:
        if len(heap) == 0:
            continue
        else:
            heapq.heappop(heap)
