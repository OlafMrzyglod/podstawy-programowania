x = float(input("x = "))
y = float(input("y = "))
point = f"P({x:g},{y:g})"
if x == 0 and y == 0:
    print(f"Point {point} is at the origin")
elif y == 0:
    print(f"Point {point} is on the X axis")
elif x == 0:
    print(f"Point {point} is on the Y axis")
elif x > 0 and y > 0:
    print(f"Point {point} is in the first quadrant")
elif x < 0 and y > 0:
    print(f"Point {point} is in the second quadrant")
elif x < 0 and y < 0:
    print(f"Point {point} is in the third quadrant")
else:
    print(f"Point {point} is in the fourth quadrant")
