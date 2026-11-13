n = int(input("Enter how many prime numbers to print: "))
found = 0
candidate = 2
print("Prime numbers:", end=" ")
while found < n:
    divisor = 2
    is_prime = True
    while divisor * divisor <= candidate:
        if candidate % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(candidate, end=" ")
        found += 1
    candidate += 1
print()
