with open('input.txt', 'r') as file:
    total = 0
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        result = line.split(',')
        one = result[0].split('-')
        two = result[1].split('-')
        result = [one[0], one[1], two[0], two[1]]
    
        a_lowbound, a_highbound = int(result[0]), int(result[1])
        b_lowbound, b_highbound = int(result[2]), int(result[3])
        result1 = a_lowbound <= b_lowbound <= b_highbound <= a_highbound
        result2 = b_lowbound <= a_lowbound <= a_highbound <= b_highbound
        if result1 or result2 == True:
            total += 1

print(total)