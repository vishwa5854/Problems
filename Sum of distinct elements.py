T = int(input())
for z in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    C = set()
    for i in arr:
        C.add(i)
    print(sum(C))
