T = int(input())
for z in range(T):
    N = int(input())
    b = bin(N).replace("0b", "").count("0")
    print((1 << b) - 1)
