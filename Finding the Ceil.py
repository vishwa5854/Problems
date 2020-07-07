def BS(A, n, target):
    low = 0
    high = n - 1
    ans = 2147483647
    while low <= high:
        mid = (low + high) // 2
        if A[mid] >= target:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans


N = int(input())
arr = sorted(list(map(int, input().split())))
Q = int(input())
for i in range(Q):
    q = int(input())
    print(BS(arr, N, q))
