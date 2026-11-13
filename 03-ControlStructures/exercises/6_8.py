name1 = input("Enter first person's name: ")
age1 = int(input("Enter first person's age: "))
name2 = input("Enter second person's name: ")
age2 = int(input("Enter second person's age: "))
if age1 >= 18 and age2 >= 18:
    print(f"Both {name1} and {name2} are adults")
else:
    print(f"Either {name1} or {name2} is not an adult")