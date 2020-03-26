a = input()
ans = 0
if len(a) % 2 == 1:
    mid = int(len(a) / 2) + 1
    for i in range(mid*2 - 2, 0, -1):
        if a[:i] == a[len(a) - i:len(a)]:
            ans = i
            break
else:
    mid = int(len(a) / 2)
    for i in range(mid*2 - 2, 0, -1):
        if a[:i] == a[len(a) - i:len(a)]:
            ans = i
            break

print(ans)
