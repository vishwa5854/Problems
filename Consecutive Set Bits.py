T = int(input())
for z in range(T):
    N = int(input())
    b = sorted((bin(N).replace("0b", "")).split("0"))
    print(len(b[len(b) - 1]))
