quantity = int(input("Number of products purchased: "))
price = float(input("Product price: "))
if quantity <= 2:
    total = quantity * price
else:
    total = 2 * price + (quantity - 2) * price * 0.75
print(f"Amount to pay: {total:.2f}")
