for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

#1+2+3+4
sum=0
for i in range(1,5):
    sum=sum+i
print(str(sum))


n = int(input("number of stars: "))
stars = ""
for s in range(0,n):
    stars = stars + "*"
print(stars)
