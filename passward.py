userpass = {}

while True:
    user = input("Your name")
    pwd = input("Your password")

    if user in userpass and pwd == userpass[user]:
        print("Welcome", user)
        break
    else:
        userpass[user]=pwd
        print("registration completed,please login")
