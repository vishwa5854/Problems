T = int(input())
for z in range(T):
    print("Case #" + str(z + 1) + ":")
    a = int(input())
    a = int(a / 2)
    print(" " * a + "*")
    for i in range(1, a + 1):
        print(" " * (a - i) + "*" + "  " * (i - 1) + " *")
    for i in range(a - 1, 0, -1):
        print(" " * (a - i) + "*" + "  " * (i - 1) + " *")
    print(" " * a + "*")
