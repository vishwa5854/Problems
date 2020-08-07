T = int(input())
for z in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = set()
    for i in A + B:
        C.add(i)
    print(len(C))
