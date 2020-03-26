n = int(input())
for i in range(n):
    lol = input()
    l = int(len(lol)/2)
    a = lol[:l]
    b = lol[l+len(lol)%2:]
    
    print(a)

    print(b)
    if a == b:
        print("YES")
    else:
        print("NO")
