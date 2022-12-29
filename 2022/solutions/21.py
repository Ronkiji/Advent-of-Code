inputs = [line.rstrip('\n') for line in open("inputs/21.txt")]
monk = {}
import sympy
import math
def one():
    for line in inputs:
        m, op = line.split(': ')
        # if op.isdigit():
        #     monk[m] = int(op)
        # else:
        monk[m] = op


    while not monk["root"].isdigit():

        for m, op in monk.items():
            # print(m, op)
            
            if not op.isdigit():
                # print(op)
                x, o, y = op.split(" ")
                if monk[x].isdigit() and monk[y].isdigit():
                    monk[m] = str(int(eval(monk[x] + o + monk[y])))

    print(monk["root"])

def two():

    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    monkeys = {"humn": sympy.Symbol("X")}

    q = inputs

    for monkey in q:
        # print(monkey)
        m, op = monkey.split(": ")
        
        if m in monkeys: 
            continue
        
        if op.isdigit():
            monkeys[m] = int(op)
        else:
            m1, o, m2 = op.split(" ")
            if m1 in monkeys and m2 in monkeys:
                if m == "root":
                    print(math.ceil(sympy.solve(monkeys[m1] - monkeys[m2])[0]))
                    return
                monkeys[m] = ops[o](monkeys[m1], monkeys[m2])
            else:
                q.append(monkey)
                
one()
two()