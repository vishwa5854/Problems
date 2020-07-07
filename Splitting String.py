def check(A, start, end):
    c = 0
    for i in A[start: end+1]:
        if A[start] == i:
            c += 1
    return c == (end - start+1)


def solve(a, start, end, cut, m, ansFound):
    if len(a) == 1 or check(a, start, end):
        return cut

    mid = (start + end) // 2
    cut += 1
    if ansFound:
        if cut > m:
            return cut
    a1 = solve(a, 0, mid, cut, m, ansFound)
    if not ansFound:
        m = a1
        ansFound = True
    b1 = solve(a, mid + 1, end, cut, m, ansFound)
    return min(a1, b1)


T = int(input())
for z in range(T):
    s = input()
    N = len(s)
    cuts = 0
    print(solve(s, 0, N, cuts, 0, False))
