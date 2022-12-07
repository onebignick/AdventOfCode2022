with open('input.txt', 'r') as file:
    result = file.readline()
    pointer1, pointer2 = 0, 14
    while pointer2 < len(result):
        if len(set(result[pointer1:pointer2])) == 14:
            print(pointer2)
            break
        pointer1 += 1
        pointer2 += 1