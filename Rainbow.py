T = int(input())
for z in range(T):
    N = int(input())
    a = input()
    if N < 7:
        print("No")
    else:
        if a == "VIBGYOR":
            print("Yes")
        else:
            print("No")
