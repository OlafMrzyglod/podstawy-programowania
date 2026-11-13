ean = input("Enter EAN-13 article number: ").strip()
if len(ean) == 13 and ean.isascii() and ean.isdigit():
    print("Article number is correct")
    if ean.startswith("590"):
        print("Article manufactured in Poland")
else:
    print("Incorrect article number")
