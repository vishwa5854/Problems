def prefixAndSuffix(lol):
    for i in range(int(len(lol) / 2), 0, -1):
        prefix = lol[0:i]
        suffix = lol[len(lol) - i: len(lol)]
        if prefix == suffix:
            print(i, prefix)


a = input()
prefixAndSuffix(a)
