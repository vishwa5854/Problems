def search(lol, target):
    mid = int(0 + len(lol) / 2)
    if target == lol[mid]:
        return mid
    if target > lol[mid]:
        return search(lol[mid:], target)
    if target < lol[mid]:
        return search(lol[:mid], target)
    if len(lol) == 1:
        if not target == lol[0]:
            return -1


a = list(map(int, input().split()))
b = list(map(int, input().split()))
if search(b, a[1]) == -1:
    print("false")
else:
    print("true")