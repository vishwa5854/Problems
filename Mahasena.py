numberOfSoldiers = int(input())
weapons = list(map(int, input().split()))
lucky = 0
for i in weapons:
    if i % 2 == 0:
        lucky += 1
if (numberOfSoldiers - lucky) < lucky:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
