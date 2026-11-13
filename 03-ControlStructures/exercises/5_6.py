n = int(input("Enter N: "))
sum_even = 0
number = 2
while number <= n:
    sum_even += number
    number += 2
print(f"The sum of even numbers from 1 to {n} is: {sum_even}")
