a = int(input())
meta = "* "
print(meta * a)
counter = int((a-1)/2)
for i in range(a-1, 1, -1):
    print(meta + "  "*(i-2) + meta)
print("*")
