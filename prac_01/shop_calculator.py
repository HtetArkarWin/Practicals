n = int(input("number of items: "))
sum = 0
for i in range (0,n,1):
    price=float(input("Price of Item:"))
    sum = sum + price

total=0
if sum>100:
    total = sum - (sum*0.1)
else:
    total =sum

print("Total price for {} items is ${:.2f}".format(n, total))
