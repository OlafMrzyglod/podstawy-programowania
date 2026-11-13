program = input("Select (j)acket, (u)nderwear, (s)hoes: ").lower()
extra_rinse = input("Extra rinse? (y/n): ").lower() == "y"
extra_spin = input("Extra spin? (y/n): ").lower() == "y"
if program == "j":
    total = 40
elif program == "u":
    total = 70
elif program == "s":
    total = 20
else:
    print("Incorrect washing program")
    raise SystemExit
if extra_rinse:
    total += 15
if extra_spin:
    total += 9
print(f"Total washing time: {total} minutes")
