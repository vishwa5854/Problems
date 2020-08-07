from math import log

T = int(input())
for z in range(T):
    n, k = map(int, input().split())
    print(int(log(n, k)))
