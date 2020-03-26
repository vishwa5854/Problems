T = int(input())
for z in range(T):
    Quantity, price = map(float, input().split())
    if Quantity > 1000:
        total = Quantity * price
        total -= 10/100 * total
        print(str(total)+"0"*5)
    else:
        total = Quantity * price
        print(str(total)+"0"*5)
