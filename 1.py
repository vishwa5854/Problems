def calculateProduct(lol):
    p = 1
    for a in lol:
        p *= a

    return p


numberOfTestCases = int(input())
for i in range(numberOfTestCases):
    nS, kS = input().split(" ")
    n = int(nS)
    k = int(kS)
    inp = []
    for j in input():
        inp = int(input())
    print(inp)
