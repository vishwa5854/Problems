from math import sqrt

T = int(input())
for z in range(T):
    N = int(input())
    c = 0
    repeated = 0
    s = int(sqrt(N))
    for i in range(1, s + 1):
        if N % i == 0:
            c += 1
        if i*i == N:
            repeated = 1
    print(2*c - repeated)
