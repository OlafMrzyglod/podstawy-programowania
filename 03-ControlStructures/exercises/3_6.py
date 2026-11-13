month = int(input("Enter month number (1..12): "))
day = int(input("Enter day number: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    day_ok = 1 <= day <= 31
elif month in (4, 6, 9, 11):
    day_ok = 1 <= day <= 30
elif month == 2:
    day_ok = 1 <= day <= 28
else:
    day_ok = False
message = f"Day {day} for the month {month}"
if day_ok:
    print(f"{message} is correct")
else:
    print(f"{message} is incorrect")
