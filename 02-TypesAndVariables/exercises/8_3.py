# 8.3. Przelicznik temperatury
# Wczytaj temperaturę w stopniach Celsjusza.
celsius = float(input("Enter temperature in Celsius: "))
# Przelicz temperaturę na kelwiny i stopnie Fahrenheita.
kelvin = celsius + 273.15
fahrenheit = celsius * 9 / 5 + 32
# Wyświetl oba wyniki.
print(f"Kelvin: {kelvin:.2f} K")
print(f"Fahrenheit: {fahrenheit:.2f} °F")