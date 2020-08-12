def check(lol, start, end):
    arr = set()
    for i in range(start, end):
        if lol[i] in arr:
            return False
        arr.add(lol[i])
    return True


def length_of_longest_substring(s):
    ans = 1
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if check(s, i, j):
                ans = max(ans, j - i + 1)
    return ans


def length_of_longest_substring_optimal(s):
    if s == "":
        return 0
    ans = 1
    i = 0
    j = 0
    lol = set()
    while j < len(s):
        if s[j] not in lol:
            lol.add(s[j])
            j += 1
            ans = max(ans, len(lol))
        else:
            lol.remove(s[i])
            i += 1
    return ans


if __name__ == '__main__':
    a = input()
    print(length_of_longest_substring(a))
