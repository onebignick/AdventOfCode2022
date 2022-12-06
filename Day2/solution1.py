# A: Rock B: Paper C: Scissors
# X: Rock Y: Paper Z: Scissors

hashtable = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3,
    "A" : 1,
    "B" : 2,
    "C" : 3,
    2 : 1,
    3 : 2,
    1 : 3,
}
with open('input.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.strip()
        data = line.split(' ')
        data = [hashtable[data[0]], hashtable[data[1]]]

        total += data[1]
        if data[0] == data[1]:
            total += 3
        elif data[0] == hashtable[data[1]]:
            total += 6
        else:
            total += 0

print(total)