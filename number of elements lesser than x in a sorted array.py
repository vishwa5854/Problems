def small(arr, N, x):
    low = 0
    high = N - 1
    c = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            high = mid - 1
        else:
            c += mid - 1
            low = mid + 1
    return c


print(small(list(map(int, input().split())), int(input()), int(input())))
