# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
volume = a * b * c
surface_area = 2 * (a * b + a * c + b * c)
print(f"Volume: {volume:g}")
print(f"Surface area: {surface_area:g}")