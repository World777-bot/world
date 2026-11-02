# Byte Stuffing

flag = input("Enter FLAG: ")
esc = input("Enter ESC: ")

n = int(input("Enter number of bytes: "))

frame = []

for i in range(n):
    byte = input("Enter byte: ")
    frame.append(byte)

stuffed = []

for byte in frame:
    if byte == flag or byte == esc:
        stuffed.append(esc)

    stuffed.append(byte)

print("\nOriginal Frame:")
print(*frame)

print("\nStuffed Frame:")
print(*stuffed)