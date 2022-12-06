# Open file
with open('input.txt', 'r') as file:
    data = file.readlines()
    base, total = 0, 0
    for line in data:
        # Check if line is empty
        if line.strip():
            total += int(line)
        else:
            # Check if elf is highest elf
            if total >= base:
                base = total
            # Repeat
            total = 0
    
print(base)
# Output: 70116

