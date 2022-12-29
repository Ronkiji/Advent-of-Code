inputs = [line.rstrip('\n') for line in open("inputs/10.txt")]

commands = {}
cycle = 1
for x in range (len(inputs)):
    num = 0
    if inputs[x].__contains__(" "):
        num = int(inputs[x].split(" ")[1])
        cycle += 1
    if num != 0:
        commands[tracker] = num
    cycle += 1

def one():
    
    check = [20, 60, 100, 140, 180, 220]
    register = 1
    total = []
    for cycle in range (1, max(check) + 2):
        if cycle in check:
            total.append(register * cycle)
        if cycle in commands.keys():
            register += commands[cycle]
            
    print(sum(total))

def two():

    pixel = 1
    register = 1
    sprite = (1,2,3)
    strings = []
    string = ""
    
    x = 1
    for six in range(6):
        for cycle in range(x, x+40):
            
            if pixel in sprite:
                string += "#"
            else:
                string += "."
            if cycle in commands.keys():
                register += commands[cycle]
                sprite = (register, register + 1, register + 2)
            pixel += 1
        strings.append(string)
        string = ""
        x += 40
        pixel = 1

    for string in strings:
        print(string)

one()
two()