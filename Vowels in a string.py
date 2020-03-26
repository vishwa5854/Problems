vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
a = input()
ans = "Yes"
for i in a:
    if i not in vowels:
        ans = "No"
        break
print(ans)
