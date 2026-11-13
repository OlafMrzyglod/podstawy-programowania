swift = input("Enter SWIFT code: ").strip().upper()
print(f"Bank Code: {swift[:4]}")
print(f"Country Code: {swift[4:6]}")