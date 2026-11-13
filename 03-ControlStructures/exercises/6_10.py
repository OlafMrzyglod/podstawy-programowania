age = float(input("Enter the dog's age in human years: "))
if age <= 2:
    dog_years = age * 10.5
else:
    dog_years = 21 + (age - 2) * 4
print(f"The dog's age in dog's years is {dog_years:g} years.")
