a = int(input())
for i in range(a):
    temp = ""
    for j in range(i+1):
        temp += chr(j + 65) + " "
    temp2 = temp[:len(temp)-3]
    if not i == 0:
        temp += temp2[::-1]
    print(temp)
