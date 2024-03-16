email = input("what is your email address: ")
e = "@" in email
if e:
    print("the email is valid")
else:
    print("email is invalid")