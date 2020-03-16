length = int(input())
lol = list(map(int, input().split()))
unique = []
for i in range(length):
    if i < length:
        temp = lol[i]
        lol[i] = "!"
        if temp not in lol:
            unique.append(temp)
        lol[i] = temp
print(unique)
