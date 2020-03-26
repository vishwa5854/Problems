a = input()
uniq = []
for i in a:
    if i not in uniq:
        uniq.append(i)
if len(uniq) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
