numberOfTestCases = int(input())
for z in range(numberOfTestCases):
    dictSize = int(input())
    dictionary = input().split()
    inp = input()
    inp += "~"
    temp = inp
    output = []
    count = 0
    while True:
        op = ""
        while inp != "~":
            for i in dictionary:
                if inp.startswith(i):
                    op += i + " "
                    dictionary.remove(i)
                    dictionary.append(i)
                    inp = inp[len(i):]
        inp = temp
        if op in output:
            break
        count += 1
        output.append(op)
    for i in output:
        print(i)
