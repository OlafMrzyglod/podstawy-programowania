# 7.4. Średnica drzewa obliczona z obwodu
import math

circumference = float(input("Enter tree circumference in cm: "))
diameter = circumference / math.pi
print(f"Tree can be cut down: {diameter >= 50}")