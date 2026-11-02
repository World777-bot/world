
# Autokey Cipher

text = input("Enter plaintext: ").lower()
key = 7

# Remove spaces
text = text.replace(" ", "")

# Convert plaintext into numbers (A=0 to Z=25)
p_values = [ord(ch) - ord('a') for ch in text]

# Generate key stream: Initial key + plaintext values
key_stream = [key] + p_values[:-1]

# Encryption
encrypted = ""

print("\nENCRYPTION STEPS")
print("Formula: C = (P + K) % 26\n")

for i in range(len(text)):
    p = p_values[i]
    k = key_stream[i]
    c = (p + k) % 26

    encrypted += chr(c + ord('a'))

    print(text[i].upper(), "+", k, 
          "=", c, "->", chr(c + ord('a')).upper())

print("\nEncrypted Text:", encrypted.upper())

# Decryption
decrypted = ""

print("\nDECRYPTION STEPS")
print("Formula: P = (C - K) % 26\n")

for i in range(len(encrypted)):
    c = ord(encrypted[i]) - ord('a')

    if i == 0:
        k = key
    else:
        k = ord(decrypted[i-1]) - ord('a')

    p = (c - k) % 26
    decrypted += chr(p + ord('a'))

    print(encrypted[i].upper(), "-", k,
          "=", p, "->", chr(p + ord('a')).upper())

print("\nDecrypted Text:", decrypted.upper())
