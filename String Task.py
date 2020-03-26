vowels = ["a", "e", "i", "o", "u", "A", "E", "I", 'O', "U", "y", "Y"]
lol = input()
lol = lol.lower()
ans = ""
for i in lol:
    if i not in vowels:
        ans += "." + i
print(ans)
