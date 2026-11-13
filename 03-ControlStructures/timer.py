###
# Takes a number from the user and counts down to zero.
#
# Modify the program so that the last five seconds of the counter
# are displayed in words, i.e. five, four, three, two, one.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

words = {5: "five", 4: "four", 3: "three", 2: "two", 1: "one"}

while countdown > 0:
    print(words.get(countdown, countdown), flush=True)  
    # get() zwraca słowo ze słownika dla danej liczby, a gdy jej brak, zwraca countdown. flush=True wymusza natychmiastowe wypisanie wyniku.
    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")
