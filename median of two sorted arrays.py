def s(a, n, x):
    lo = 0
    hi = n - 1
    c = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] >= x:
            hi = mid - 1
        else:
            c += mid + 1
            lo = mid + 1
    return c


def g(a, n, x):
    lo = a[0]
    hi = a[n - 1]
    c = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            hi = mid - 1
        else:
            c += mid + 1
            lo = mid + 1
    return c


T = int(input())
for z in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    low = min(A[0], B[0])
    high = max(A[N - 1], B[M - 1])
    while low <= high:
        mid = (low + high) // 2
        small = s(A, N, mid) + s(B, M, mid)
        greater = g(A, N, mid) + g(B, M, mid)
        if small > greater:
            high = mid - 1
        elif greater > small:
            low = mid + 1
        else:
            print(mid)
            break
