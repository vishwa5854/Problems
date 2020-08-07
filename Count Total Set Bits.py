a = int(input())
c = 0
for i in range(1, a + 1):
    a = bin(i).replace("0b", "")
    c += a.count("1")
print(c)
