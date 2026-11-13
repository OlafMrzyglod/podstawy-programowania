try:
    hour, minute = map(int, input("Enter time (24-hour format): ").split(":"))
except ValueError:
    print("Incorrect time")
    raise SystemExit
if 0 <= hour <= 23 and 0 <= minute <= 59:
    period = "am" if hour < 12 else "pm"
    hour_12 = hour % 12 or 12
    print(f"Time in 12-hour format: {hour_12}:{minute:02d}{period}")
else:
    print("Incorrect time")
