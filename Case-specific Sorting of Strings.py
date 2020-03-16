numberOfTestCases = int(input())
for z in range(numberOfTestCases):
    w = input()
    lol = input()
    small = ""
    caps = ""
    output = ""
    for i in lol:
        if i.isupper():
            caps += i
        if i.islower():
            small += i
    small = sorted(small)
    caps = sorted(caps)
    for i in lol:
        if i.isupper():
            output += caps[0]
            caps = caps[1:]
        elif i.islower():
            output += small[0]
            small = small[1:]
    print(output)
