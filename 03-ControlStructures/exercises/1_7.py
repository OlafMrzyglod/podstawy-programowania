basic_salary = 5000
is_bonus = input("Does the employee receive a bonus? (Y/N): ").upper() == "Y"
total_salary = basic_salary
if is_bonus:
    bonus = float(input("Bonus percentage: "))
    total_salary += basic_salary * bonus / 100
print(f"Basic salary: {basic_salary:.2f} PLN")
print(f"Bonus included? {is_bonus}")
print(f"Total salary: {total_salary:.2f} PLN")
