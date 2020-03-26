from math import factorial as fact


def nCr(n, r):
    return fact(n) / (fact(r) * fact(n - r))


T = int(input())
for z in range(T):
    N = int(input())
    lol = list(map(int, input().split()))
    numberOfZeroes = 0
    numberOfTwos = 0
    for i in lol:
        if i == 0:
            numberOfZeroes += 1
        if i == 2:
            numberOfTwos += 1
    ans = 0
    if numberOfTwos >= 2:
        ans += nCr(numberOfTwos, 2)
    if numberOfZeroes >= 2:
        ans += nCr(numberOfZeroes, 2)
    print(int(ans))
