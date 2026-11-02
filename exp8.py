# Byte Stuffing (Character Stuffing)

# Accept input from user
A = input("Enter A: ")
B = input("Enter B: ")
FLAG = input("Enter FLAG: ")
ESC = input("Enter ESC: ")

# Original frame
frame = [A, B, ESC, FLAG]

print("\nOriginal Frame:")
print(*frame)

# Perform Byte Stuffing
stuffed_frame = []

for byte in frame:

    # Insert ESC before FLAG or ESC
    if byte == FLAG or byte == ESC:
        stuffed_frame.append(ESC)

    stuffed_frame.append(byte)

# Display stuffed frame
print("\nStuffed Frame:")
print(*stuffed_frame)