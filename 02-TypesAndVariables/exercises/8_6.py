# 8.6. Koszt paliwa na trasie
distance = float(input("Enter distance in km: "))
fuel_price = float(input("Enter fuel price per liter: "))
fuel_consumption = float(input("Enter fuel consumption in liters per 100 km: "))
total_fuel_consumption = distance / 100 * fuel_consumption
total_cost = total_fuel_consumption * fuel_price
print(f"Fuel used: {total_fuel_consumption:.2f} L")
print(f"Total cost: {total_cost:.2f}")