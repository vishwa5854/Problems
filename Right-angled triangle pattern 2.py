a = int(input())
c = 0
for i in range(1, a + 1):
    if i == 1:
        print(1)
    else:
        z = 1
        ans = i
        for j in range(i):
            print(ans, end=" ")
            ans += a - z
            z += 1
        print()
