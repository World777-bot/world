# Character Count Framing

# Accept number of data bytes
n = int(input("Enter number of data bytes: "))

frame = []

# Accept data bytes
for i in range(n):
    byte = input("Enter byte: ")
    frame.append(byte)

# Calculate total count (including count field)
count = n + 1

# Display transmitted frame
print("\nOriginal Data:")
print(*frame)

print("\nCharacter Count:", count)

print("\nTransmitted Frame:")
print(count, *frame)