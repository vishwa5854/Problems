numberOfTestCases = int(input())
for z in range(numberOfTestCases):
    n = int(input())
    lol = list(map(int, input().split()))
    reset = n - 1
    i = 0
    while True:
        if i == reset:
            i = 0
        if lol[i] == 0:
            print(i+1)
            break
        else:
            for j in range(len(lol)):
                lol[j] -= 1
            i += 1
