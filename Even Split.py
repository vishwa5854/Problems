T = int(input())
for z in range(T):
    N = int(input())
    if N <= 2:
        print("No")
    elif N % 2 == 0:
        print("Yes")
    else:
        print("No")
