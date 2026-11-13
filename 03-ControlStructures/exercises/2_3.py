mode = input("Driving mode (A/M/E): ").strip().upper()
if mode == "A":
    consumption = 7
elif mode == "M":
    consumption = 9
elif mode == "E":
    consumption = 6
else:
    print("Incorrect driving mode")
    raise SystemExit
distance = float(input("Distance in km: "))
total = distance * consumption / 100
print(f"Total fuel consumption over {distance:g} km in mode {mode}: {total:g} liters")
