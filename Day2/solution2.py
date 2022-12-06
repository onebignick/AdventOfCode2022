# A: Rock B: Paper C: Scissors
# X: Lose Y: Draw Z: Win

hashtable = {
    "A": 1,
    "B": 2,
    "C": 3,
}

hashtable_win = {
    "A": "B",
    "B": "C",
    "C": "A",
}

hashtable_lose = {
    "A": "C",
    "B": "A",
    "C": "B",
}

with open('input.txt', 'r') as file:
    lines = file.readlines()
    total = 0
    for line in lines:
        line = line.strip()
        data = line.split(' ')
        if data[1] == 'X':
            total += hashtable[hashtable_lose[data[0]]]
        elif data[1] == 'Y':
            total += (hashtable[data[0]] + 3)
        else:
            total += (hashtable[hashtable_win[data[0]]] + 6)

print(total)