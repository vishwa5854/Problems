a = input()
if a[0] == "-":
    temp = a[1:]
    print("-"+str(int(temp[::-1])))
else:
    print(int(a[::-1]))
