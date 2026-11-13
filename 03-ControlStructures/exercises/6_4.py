password = input("Enter new password: ")
if len(password) < 12:
    print("Password too short (min. 12 chars)")
else:
    print("Password length is correct")
