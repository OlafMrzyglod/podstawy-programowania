current_price = int(input("New price: "))
previous_price = 200
reduction = (previous_price - current_price) / previous_price
print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")
if reduction >= 0.10:
    print("Buy the product!!")
    print(f"Product price reduced by {reduction:.0%}")
