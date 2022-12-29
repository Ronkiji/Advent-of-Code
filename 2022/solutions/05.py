inputs = [line.rstrip('\n') for line in open("inputs/05.txt")]

def one():
    stacks = []

    rows = 8
    cols = 9
    start = 10

    for i in range(cols):
        stacks.append([])

    for i in range(rows): # rows
        for j in range(cols): # columns
            if inputs[i][1 + (4 * j)] != " ":
                stacks[j].append(inputs[i][1 + (4 * j)])

    for i in range(cols):
        stacks[i].reverse()

    for i in range(start, len(inputs)):
        left, right = inputs[i].split(" from ")
        move, num = left.split(" ")
        fr, to = right.split(" to ")
        
        for x in range(int(num)):
            stacks[int(to)-1].append(stacks[int(fr)-1].pop())

    answer = ""
    for stack in stacks:
        answer += stack[-1]

    print(answer)

def two():
    stacks = []

    rows = 8
    cols = 9
    start = 10

    for i in range(cols):
        stacks.append([])

    for i in range(rows): # rows
        for j in range(cols): # columns
            if inputs[i][1 + (4 * j)] != " ":
                stacks[j].append(inputs[i][1 + (4 * j)])

    for i in range(cols):
        stacks[i].reverse()

    for i in range(start, len(inputs)):
        left, right = inputs[i].split(" from ")
        move, num = left.split(" ")
        fr, to = right.split(" to ")
        
        for x in range(int(num), 0, -1):
            stacks[int(to)-1].append(stacks[int(fr)-1][-x])

        for x in range(int(num)):
            stacks[int(fr)-1].pop()

    answer = ""
    for stack in stacks:
        answer += stack[-1]

    print(answer)

one()
two()