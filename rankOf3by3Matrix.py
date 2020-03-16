import  numpy


def calculateDeterminant3by3(inp):
    return inp[0][0] * (inp[1][1] * inp[2][2] - inp[1][2] * inp[2][1]) - inp[0][1] * (
            inp[1][0] * inp[2][2] - inp[2][0] * inp[1][2]) + inp[0][2] * (
                   inp[1][0] * inp[2][1] - inp[1][1] * inp[2][0])


def calculateDeterminant2by2(inp):
    return inp[0][0] * inp[1][1] - inp[0][1] * inp[1][1]


numberOfTestCases = int(input())
output = []
for z in range(numberOfTestCases):
    arr = []
    for x in range(3):
        temp = input().split(" ")
        arr.append(temp)

    if calculateDeterminant3by3(arr) != 0:
        output.append(3)
    else:
        output.append("either 2 or 1")
print(output)
