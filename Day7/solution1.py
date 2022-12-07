class Node:
    def __init__(self, title, total):
        self.title = title
        self.total = total
        self.next = None

prev, answer = None, 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(' ')
        if line[1] == 'cd':
            if line[2] == '..':
                temp = cur
                prev, cur = prev.next, cur.next
                cur.total += temp.total
                if temp.total <= 100000:
                    answer+=temp.total
            else:
                cur = Node(line[2], 0)
                cur.next = prev
                prev = cur
        elif line[0].isnumeric() == True:
            cur.total += int(line[0])

if cur.total <= 100000:
    answer += cur.total

print(answer)
