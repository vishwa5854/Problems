T = int(input())
for z in range(T):
    lol = int(input())
    if lol == 0:
        print(1)
    if lol == 1:
        print(1)
    else:
        a = 1
        b = 1
        for i in range(2, lol):
            c = a + b
            a = b
            b = c
        print(b % 1000000007)
