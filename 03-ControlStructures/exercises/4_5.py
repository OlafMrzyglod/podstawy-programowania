plain_text = "The early bird catches the worm"
encrypted_text = ""
for char in plain_text:
    if "A" <= char <= "Z":
        base = ord("A")
        char = chr(base + (ord(char) - base + 1) % 26)
    elif "a" <= char <= "z":
        base = ord("a")
        char = chr(base + (ord(char) - base + 1) % 26)
    encrypted_text += char
print(plain_text)
print(encrypted_text)
