# 7.5. Prefiks rejestracji
car_number = input("Enter car registration number: ").strip().upper()
prefix = car_number[:2]
is_krakow = prefix == "KR" or prefix == "KK"
print(f"Car is from Krakow: {is_krakow}")