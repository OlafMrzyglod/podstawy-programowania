# 5.5. Cena po rabacie
price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))
reduction = price * discount / 100
discounted_price = price - reduction
print(f"Original price: {price:.2f}")
print(f"Discount: {discount:g}%")
print(f"Price with discount: {discounted_price:.2f}")
print(f"Reduction: {reduction:.2f}")