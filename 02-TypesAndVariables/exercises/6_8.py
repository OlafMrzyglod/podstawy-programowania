first = input("Enter first letter: ").strip().upper()
last = input("Enter second letter: ").strip().upper()
number_of_letters = max(0, abs(ord(last) - ord(first)) - 1)
print(f"Letters between {first} and {last}: {number_of_letters}")