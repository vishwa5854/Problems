def GCD(a, b):
    if b == 0:
        return a

    if a == 0:
        return b

    return GCD(b, a % b)


T = int(input())
for z in range(T):
    ip = list(map(int, input().split()))
    g = GCD(ip[0], ip[1])
    print(int(ip[0] * ip[1] / g), g)

