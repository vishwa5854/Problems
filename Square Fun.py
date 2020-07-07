from math import sqrt


def squares(a, b):
    start = int(sqrt(a))
    end = int(sqrt(b))
    if start ** 2 < a:
        start += 1
    if end ** 2 > b:
        end -= 1
    return end - start + 1


T = int(input())
for z in range(T):
    A, B = map(int, input().split())
    ans = squares(A, B)
    print(ans)
