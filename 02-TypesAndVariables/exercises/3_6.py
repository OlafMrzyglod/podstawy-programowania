# 3.6. Odległość do horyzontu
import math

height = float(input("Enter observer height in meters: "))
distance = 3.57 * math.sqrt(height)
print(f"Distance to the horizon: {distance:.2f} km")