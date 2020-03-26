prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
prices = prices[::-1]
T = int(input())
for z in range(T):
    p = int(input())
    c = 0
    while p > 0:
        for i in prices:
            if p >= i:
                p -= i
                c += 1
                break
    print(c)
