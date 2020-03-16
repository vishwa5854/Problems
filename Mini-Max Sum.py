def miniMaxSum(arr):
    arr = sorted(arr)
    mn = 0
    l = len(arr)
    for i in range(l-1):
        mn += arr[i]
    mx = mn - arr[0] + arr[l - 1]
    print(mn, mx)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
