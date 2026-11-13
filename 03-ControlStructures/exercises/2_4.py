a = float(input("First number: "))
b = float(input("Second number: "))
operator = input("Operator (+, -, *, /): ").strip()
if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/" and b != 0:
    result = a / b
else:
    print("Cannot divide by zero" if operator == "/" else "Incorrect operator")
    raise SystemExit
print(f"{a:g} {operator} {b:g} = {result:g}")
