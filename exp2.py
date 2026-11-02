
# Affine Cipher

text = input("Enter plaintext: ").lower()

a = 7
b = 2
a_inv = 15

text = text.replace(" ", "")

# Encryption
encrypted = ""

print("\nENCRYPTION STEPS")
print("Formula: C = (a * P + b) % 26")

for ch in text:
    p = ord(ch) - ord('a')
    c = (a * p + b) % 26
    encrypted += chr(c + ord('a'))

    print(ch, ":", p, "->", 
          "(", a, "*", p, "+", b, ") % 26 =", c,
          "->", chr(c + ord('a')).upper())

print("\nEncrypted Text:", encrypted.upper())

# Decryption
decrypted = ""

print("\nDECRYPTION STEPS")
print("Formula: P = a_inv * (C - b) % 26")
print("Multiplicative inverse =", a_inv)

for ch in encrypted:
    c = ord(ch) - ord('a')
    p = (a_inv * (c - b)) % 26
    decrypted += chr(p + ord('a'))

    print(ch, ":", c, "->",
          a_inv, "* (", c, "-", b, ") % 26 =", p,
          "->", chr(p + ord('a')).upper())

print("\nDecrypted Text:", decrypted.upper())
