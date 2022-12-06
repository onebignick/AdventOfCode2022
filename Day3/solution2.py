with open('input.txt', 'r') as file:
    test = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    store = []
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        store.append(line)
        if len(store) == 3:
            a = set(store[0]).intersection(set(store[1]))
            b = set(store[1]).intersection(set(store[2]))
            ans = a.intersection(b).pop()
            i = 0
            for char in test:
                i += 1
                if ans == char:
                    total += i
                    break
            store = []

print(total)