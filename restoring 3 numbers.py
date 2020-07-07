# arr = sorted(list(map(int, input().split())))
# B = (arr[1] - arr[0] + arr[2]) // 2
# A = (arr[1] - B)
# C = arr[3] - (A + B)
# print(A, B, C)
# print(isinstance(1, int))

def beautifulDays(i, j, k):
    ans = 0
    for z in range(i, j + 1):
        print(int(str(z)[::-1]))
        if (abs(z - int(str(z)[::-1])) / k).is_integer():
            ans += 1
    return ans


a, b, c = map(int, input().split())
print(beautifulDays(a, b, c))
