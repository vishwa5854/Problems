import os


def gradingStudents(grade):

    for i in range(len(grade)):
        if 5 - grade[i] % 5 < 3 and not grade[i] < 40:
            grade[i] -= grade[i] % 5
            grade[i] += 5
    return grade


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
