inputs = [line.rstrip('\n') for line in open("inputs/06.txt")][0]

def one():
    
    cur = inputs[0:4]

    for x in range(4, len(inputs)):
        if len(set(cur)) != 4:
            cur = inputs[x-3: x+1]
        else:
            print(x)
            break

def two():

    cur = inputs[0:14]


    for x in range(14, len(inputs)):
        if len(set(cur)) != 14:
            cur = inputs[x-13: x+1]
        else:
            print(x)
            break
        
one()
two()
