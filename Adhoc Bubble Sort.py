def bubbleSort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1

    return count


T = int(input())
for x in range(T):
    waste = int(input())
    print(bubbleSort(list(map(int, input().split()))))
