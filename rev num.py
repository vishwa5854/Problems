lol = input()
if int(lol) < 0:
    print("-"+lol[len(lol):0:-1])
else:
    print(lol[::-1])

