T = int(input())
for z in range(T):
    n = int(input())
    lol = list(map(int, input().split()))
    m = min(lol)
    lol.remove(m)
    m1 = min(lol)
    print(m + m1)
