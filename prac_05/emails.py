def main():
    email_to_name={}
    email=input("Email:")
    while email!="":
        name=get_name_from_email(email)
        is_name_correct=input(f"Is your name {name}? (Y/n)")
        if not is_name_correct=="Y":
            name=input("Name:")
        email_to_name[email]=name
        email = input("Email:")

    for key,value in email_to_name.items():
        print(f"{value} ({key})")

def get_name_from_email(email):
    name = email.split("@")
    if len(name)>0:
        name=name[0]

    name = name.split(".")
    name = str.join(" ", name).title()
    return name

main()






