print("SURVEY")
computer_science = input("Are you interested in computer science? (y/n): ").lower() == "y"
computer_games = input("Do you like playing computer games? (y/n): ").lower() == "y"
instagram = input("Do you have an Instagram account? (y/n): ").lower() == "y"
print("SURVEY RESULTS")
print("Interested in computer science:", "Yes" if computer_science else "No")
print("Playing computer games:", "Yes" if computer_games else "No")
print("Has an Instagram account:", "Yes" if instagram else "No")
