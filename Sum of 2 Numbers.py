T = int(input())
for z in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    i = 0
    j = N - 1
    s = sum(arr)
    ans = "No"
    while i < j:
        if arr[i] + arr[j] < s/2:
            i += 1
        elif arr[i] + arr[j] > s/2:
            j -= 1
        else:
            ans = "Yes"
            break
    print(ans)
