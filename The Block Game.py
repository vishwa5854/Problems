T = int(input())
for z in range(T):
    a = input()
    if a == a[::-1]:
        print("wins")
    else:
        print("losses")
