class Node:
    def __init__(self, title, total):
        self.title = title
        self.total = total
        self.next = None

prev, answer, head = None, [], None
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip().split(' ')
        if line[1] == 'cd':
            if line[2] == '..':
                temp = cur
                prev, cur = prev.next, cur.next
                cur.total += temp.total
                if temp.total >= 1735494:
                    print(temp.total)
                    answer.append(temp)
            else:
                cur = Node(line[2], 0)
                if head == None:
                    head = cur
                cur.next = prev
                prev = cur
        elif line[0].isnumeric() == True:
            cur.total += int(line[0])

if cur != head:
    head.total += cur.total

if cur.total >= 1735494:
    answer.append(cur)

max = 100000000
for i in range(len(answer)):
    if answer[i].total < max:
        max = answer[i].total

#deleted = head.total - 40000000
print(max)
