
# Hill Cipher

text = input("Enter plaintext: ").lower()
text = text.replace(" ", "")

# Key matrix
key = [[3, 2],
       [5, 7]]

# Inverse key matrix
inv_key = [[3, 14],
           [9, 5]]

# Add X if plaintext length is odd
if len(text) % 2 != 0:
    text += 'x'

print("\nKey Matrix:")
for row in key:
    print(row)

# Encryption
encrypted = ""

print("\nENCRYPTION STEPS")

for i in range(0, len(text), 2):

    p1 = ord(text[i]) - ord('a')
    p2 = ord(text[i+1]) - ord('a')

    c1 = (3*p1 + 2*p2) % 26
    c2 = (5*p1 + 7*p2) % 26

    encrypted += chr(c1 + ord('a'))
    encrypted += chr(c2 + ord('a'))

    print(text[i:i+2].upper(),
          "->", c1, c2,
          "->", chr(c1+97).upper(),
          chr(c2+97).upper())

print("\nEncrypted Text:", encrypted.upper())

# Decryption
decrypted = ""

print("\nDECRYPTION STEPS")

for i in range(0, len(encrypted), 2):

    c1 = ord(encrypted[i]) - ord('a')
    c2 = ord(encrypted[i+1]) - ord('a')

    p1 = (3*c1 + 14*c2) % 26
    p2 = (9*c1 + 5*c2) % 26

    decrypted += chr(p1 + ord('a'))
    decrypted += chr(p2 + ord('a'))

    print(encrypted[i:i+2].upper(),
          "->", p1, p2,
          "->", chr(p1+97).upper(),
          chr(p2+97).upper())

print("\nDecrypted Text:", decrypted.upper())
