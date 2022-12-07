with open('input.txt', 'r') as file:
    lines = file.readlines()
    stack = []
    pruned = False
    for line in lines:
        if len(line) == 1:
            pass
        elif line[1] == "o":
            pass
            if pruned == False:
                pruned = True
                for i in range(len(stack)):
                    for j in range(len(stack[i])):
                        if stack[i][j] == ' ':
                            stack[i] = stack[i][:j]
                            break
            line = line.strip().split(' ')
            num, place, target = int(line[1]), int(line[3])-1, int(line[5])-1
            for i in range(num):
                temp = stack[place].pop()
                stack[target].append(temp)
        elif line[1].isnumeric() == True:
            pass
        else:
            index = 0
            if len(stack) == 0:
                for i in range(1, len(line), 4):
                    stack.append([line[i]])
            else:
                for i in range(1, len(line), 4):
                    stack[index].insert(0, line[i])
                    index += 1

answer = ''
for i in range(len(stack)):
    answer += stack[i][-1]

print(answer)

    