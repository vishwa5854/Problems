def solve(A, B):
    d = {}
    ans1 = -1
    ans2 = -1
    idx = 1
    for i in A:
        try:
            d[i] = min(d[i], idx)
            idx += 1
        except KeyError:
            d[i] = idx
            idx += 1
    for i in A:
        try:
            start = d[i]
            end = d[B - i]
            if end < ans2:
                ans1 = start
                ans2 = end
        except KeyError:
            pass
    if ans1 != -1 and ans2 != -1:
        return [ans1, ans2]
    return []


def another(A, B):
    d = {}
    ans1 = []
    ans2 = []
    for i in range(len(A) - 1, -1, -1):
        d[A[i]] = i + 1
    for i in A[:len(A) // 2 + 1]:
        try:
            start = d[i]
            end = d[B - i]
            ans1.append(start)
            ans2.append(end)
        except KeyError:
            pass
    if ans1 != -1 and ans2 != -1:
        return [ans1, ans2]
    return []


print(
    another([4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8],
            -3))
