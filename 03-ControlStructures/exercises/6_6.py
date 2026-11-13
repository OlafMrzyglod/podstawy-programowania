hours = int(input("Enter parking hours: "))
if hours < 1:
    print("Enter at least one hour")
elif hours <= 2:
    print("Parking fee: 5 PLN")
elif hours <= 6:
    print("Parking fee: 15 PLN")
else:
    print("Parking fee: 20 PLN")
