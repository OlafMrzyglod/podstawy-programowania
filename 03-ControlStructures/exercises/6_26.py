pin = "0805"
for i in range(3):
    if input("Enter the PIN code: ") == pin:
        print("Correct PIN")
        break
    print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")
