T = int(input())
for z in range(T):
    grade = 5
    hardness, carbonContent, tensileStrength = map(float, input().split())
    if hardness > 50 and carbonContent < 0.7 and tensileStrength > 5600:
        grade = 10
    elif hardness > 50 and carbonContent < 0.7:
        grade = 9
    elif carbonContent < 0.7 and tensileStrength > 5600:
        grade = 8
    elif hardness > 50 and tensileStrength > 5600:
        grade = 7
    elif hardness > 50 or carbonContent < 0.7 or tensileStrength:
        grade = 6
    print(grade)
