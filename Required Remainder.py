# t = int(input())
# for z in range(t):
#     x, y, n = map(int, input().split())
#     remainder = n % x
#     if remainder == y:
#         print(n)
#     else:
#         if remainder < y:
#             print(n - (x - (abs(remainder - y))))
#         else:
#             print(n - (abs(remainder - y)))
def subtract(A, element):
    for i in range(len(A)):
        if A[i] == element:
            A[i] = 1e9
        else:
            A[i] -= element
    return A


def count(A):
    c = 0
    z = 0
    for i in A:
        if i <= 1000:
            c += 1
        else:
            z += 1
    return [c, z]


n = int(input())
arr = list(map(int, input().split()))
temp = count(arr)
while temp[0] >= 1:
    arr = subtract(arr, min(arr))
    print(n - temp[1])
    temp = count(arr)
