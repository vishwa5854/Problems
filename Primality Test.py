T = int(input())
for z in range(T):
    a = int(input())
    if a == 1:
        print("no")
    elif a == 2:
        print("yes")
    elif a < 1:
        print("no")
    else:
        ans = "yes"
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                ans = "no"
        print(ans)
