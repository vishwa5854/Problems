n = int(input())
lol = []
for i in range(n):
    lol.append(int(input()))
lol = sorted(lol)
for i in range(n):
    print(lol[i])
