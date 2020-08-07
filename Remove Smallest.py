def findDifferenceElements(A):
    for i in range(len(A) - 1):
        if arr[i + 1] - arr[i] <= 1:
            return [i + 1, i]
    return []


T = int(input())
for z in range(T):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    while True:
        if (len(arr) > 1) and (findDifferenceElements(arr) == []):
            print("NO")
            break
        elif len(arr) > 1:
            a = findDifferenceElements(arr)
            a.remove(min(arr[a[0]], arr[a[1]]))
        else:
            print("YES")
            break
