T = int(input())
for z in range(T):
    a = list(input().split())
    if a[2] == "+":
        print(int(a[0]) + int(a[1]))
    else:
        print(int(a[0]) - int(a[1]))
