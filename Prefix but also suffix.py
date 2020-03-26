def prefixAndSuffix(lol):
    for i in range(int(len(lol) / 2), -1, -1):
        prefix = lol[0:i + 1]
        suffix = lol[len(lol) - i - 1: len(lol)]
        if prefix == suffix:
            return i+1
    return 0


a = input()
print(prefixAndSuffix(a))
