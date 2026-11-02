
# Vigenere Cipher

text = input("Enter plaintext: ").lower()
key = input("Enter keyword: ").lower()

# Remove spaces
text = text.replace(" ", "")

# Repeat keyword
key = (key * (len(text) // len(key) + 1))[:len(text)]

# Encryption
encrypted = ""

print("\nENCRYPTION STEPS")

for i in range(len(text)):
    p = ord(text[i]) - ord('a')
    k = ord(key[i]) - ord('a')

    c = (p + k) % 26
    encrypted += chr(c + ord('a'))

    print(text[i].upper(), "+", key[i].upper(),
          "=", chr(c + ord('a')).upper())

print("\nEncrypted Text:", encrypted.upper())

# Decryption
decrypted = ""

print("\nDECRYPTION STEPS")

for i in range(len(encrypted)):
    c = ord(encrypted[i]) - ord('a')
    k = ord(key[i]) - ord('a')

    p = (c - k) % 26
    decrypted += chr(p + ord('a'))

    print(encrypted[i].upper(), "-", key[i].upper(),
          "=", chr(p + ord('a')).upper())

print("\nDecrypted Text:", decrypted.upper())
