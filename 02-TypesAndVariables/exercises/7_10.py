import random

computer = random.randint(1, 6)
you = int(input("Guess a number from 1 to 6: "))
print(f"The number is: {computer}")
print(f"You won: {you == computer}")