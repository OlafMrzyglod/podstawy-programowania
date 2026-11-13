number = int(input("Enter decimal number: "))
remaining = abs(number)
binary = ""
while remaining:
    binary = str(remaining % 2) + binary
    remaining //= 2
if not binary:
    binary = "0"
if number < 0:
    binary = "-" + binary
print(f"{number}(10) = {binary}(2)")
