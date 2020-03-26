a = input()
temp = []
res = ""
lol = a[0]
a += "~"
for i in a:
    if lol == i:
        temp.append(i)
    else:
        res += temp[0] + str(len(temp))
        temp = [i]
        lol = i
print(res)
