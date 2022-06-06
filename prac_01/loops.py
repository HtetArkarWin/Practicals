for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("number of stars: "))
stars = ""
for s in range(0,n):
    stars = stars + "*"
print(stars)

n = int(input("number of stars: "))

for i in range(0,n):
    stars = ""
    for s in range(0,i+1):
        stars = stars + "*"
    print(stars)

