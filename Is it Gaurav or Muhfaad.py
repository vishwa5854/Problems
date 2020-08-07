T = int(input())
M = [0]*26
G = [0]*26
for i in "MUHFAAD".lower():
    M[ord(i) - 97] += 1
for i in "GAURAV".lower():
    G[ord(i) - 97] += 1
for z in range(T):
    a = input().lower()
    A = [0]*26
    for i in a:
        A[ord(i) - 97] += 1
    if A == M:
        print("MUHFAAD")
    elif A == G:
        print("GAURAV")
    else:
        print("YE KAUNSA JAWAAB HUA")
