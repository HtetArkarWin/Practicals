MIN_LENGTH = 2


password = input("> ")
while len(password)<MIN_LENGTH:
    print("Password must be at least {} characters".format(MIN_LENGTH))
    password = input("> ")

stars = ""
for n in range (len(password)):
    stars = stars + "*"
print(stars)