# Open input file
with open('input.txt', 'r') as file:
    data = file.readlines()
    top3, total = [0,0,0], 0
    for line in data:
        # Check if line is empty
        if line.strip():
            # Calculate each elf total
            total += int(line)
        else:
            # Check if in top 3
            if total > top3[2]:
                top3[2] = total
                top3.sort(reverse=True)
            # Repeat
            total = 0

# top3: [70116, 68706, 67760]
print(sum(top3))
# Output: 206582