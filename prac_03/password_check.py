MIN_LENGTH = 2
def main():

    password = get_password()

    print_asterisk(password)


def print_asterisk(password):
    stars = ""
    for n in range(len(password)):
        stars = stars + "*"
    print(stars)


def get_password():
    password = input("> ")
    while len(password) < MIN_LENGTH:
        print("Password must be at least {} characters".format(MIN_LENGTH))
        password = input("> ")
    return password


main()
