phone = input("Enter phone number: ").strip()  # Pobiera numer jako tekst i usuwa białe znaki z początku i końca.
while not (phone.isascii() and phone.isdigit()):  # Powtarza pętlę, dopóki numer nie składa się wyłącznie z cyfr 0–9. isascii() sprawdza znaki ASCII, isdigit() sprawdza cyfry, a not odwraca wynik warunku.
    print("Use digits only.")  # Wyświetla komunikat, gdy wpisany numer jest niepoprawny.
    phone = input("Enter phone number: ").strip()  # Pobiera numer ponownie i zastępuje poprzednią wartość, aby pętla mogła sprawdzić nowy wpis.
print(phone)  # Wyświetla zaakceptowany numer.
print(f"Phone number: {phone[:3]}-{phone[3:6]}-{phone[6:]}")  # Dzieli numer na pierwsze 3 cyfry, kolejne 3 i resztę, łącząc je myślnikami.
