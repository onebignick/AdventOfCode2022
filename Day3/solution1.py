with open('input.txt', 'r') as file:
    test = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    lines = file.readlines()
    for line in lines:
        a = set(line[:len(line)//2])
        b = set(line[len(line)//2:])
        ans = a.intersection(b).pop()
        i = 0
        for char in test:
            i += 1
            if ans == char:
                total += i
                break

print(total)
    
