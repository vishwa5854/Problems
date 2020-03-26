N = int(input())
player1 = []
player2 = []
for i in range(N):
    temp = list(map(int, input().split()))
    player1.append(temp[0])
    player2.append(temp[1])

for i in range(1, N):
    player1[i] += player1[i - 1]
    player2[i] += player2[i - 1]

lead = {}
for i in range(N):
    if player1[i] > player2[i]:
        lead[abs(player1[i] - player2[i])] = 1
    else:
        lead[abs(player1[i] - player2[i])] = 2
m = max(list(lead.keys()))
print(lead[m], m)
