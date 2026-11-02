
# Playfair Cipher

text = input("Enter plaintext: ").lower()
key = "guidance"

# Remove spaces and replace j with i
text = text.replace(" ", "").replace("j", "i")

# Create 5x5 matrix
alphabet = "abcdefghiklmnopqrstuvwxyz"
letters = ""

for ch in key + alphabet:
    if ch not in letters:
        letters += ch

matrix = [list(letters[i:i+5]) for i in range(0, 25, 5)]

print("\nPLAYFAIR KEY MATRIX")
for row in matrix:
    print(row)

# Find position of each letter
def position(ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

# Create pairs
pairs = []
i = 0

while i < len(text):
    a = text[i]

    if i + 1 == len(text):
        b = 'x'
        i += 1
    elif text[i] == text[i+1]:
        b = 'x'
        i += 1
    else:
        b = text[i+1]
        i += 2

    pairs.append(a + b)

print("\nPLAINTEXT PAIRS:", pairs)

# Encryption
encrypted = ""

print("\nENCRYPTION STEPS")

for pair in pairs:
    a, b = pair[0], pair[1]
    r1, c1 = position(a)
    r2, c2 = position(b)

    if r1 == r2:
        x = matrix[r1][(c1+1) % 5]
        y = matrix[r2][(c2+1) % 5]

    elif c1 == c2:
        x = matrix[(r1+1) % 5][c1]
        y = matrix[(r2+1) % 5][c2]

    else:
        x = matrix[r1][c2]
        y = matrix[r2][c1]

    encrypted += x + y
    print(pair.upper(), "->", (x+y).upper())

print("\nEncrypted Text:", encrypted.upper())

# Decryption
decrypted = ""

print("\nDECRYPTION STEPS")

for i in range(0, len(encrypted), 2):
    a = encrypted[i]
    b = encrypted[i+1]

    r1, c1 = position(a)
    r2, c2 = position(b)

    if r1 == r2:
        x = matrix[r1][(c1-1) % 5]
        y = matrix[r2][(c2-1) % 5]

    elif c1 == c2:
        x = matrix[(r1-1) % 5][c1]
        y = matrix[(r2-1) % 5][c2]

    else:
        x = matrix[r1][c2]
        y = matrix[r2][c1]

    decrypted += x + y
    print((a+b).upper(), "->", (x+y).upper())

print("\nDecrypted Text:", decrypted.upper())
