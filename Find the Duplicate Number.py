def solve(arr):
    temp = 1
    for i in range(2, len(arr)):
        temp ^= i
    temp1 = arr[0]
    for i in range(1, len(arr)):
        temp1 ^= arr[i]
    return temp1 ^ temp
