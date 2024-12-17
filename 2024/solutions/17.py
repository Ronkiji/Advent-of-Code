lines = [line.rstrip('\n') for line in open("inputs/17.txt")]

A = int(lines[0].split(': ')[1])
B = int(lines[1].split(': ')[1])
C = int(lines[2].split(': ')[1])

program = list(map(int, lines[4].split(': ')[1].split(',')))

def simulate(A, B=0, C=0):

    def combo(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            exit()
    p = 0 
    output = [] 
    times = 0
    while p < len(program):
        times += 1
        opcode = program[p]  
        operand = program[p + 1] 
        
        if opcode == 0: 
            deno = 2 ** combo(operand)
            A = A // deno
        elif opcode == 1: 
            B ^= operand
        elif opcode == 2:  
            B = combo(operand) % 8
        elif opcode == 3: 
            if A != 0:
                p = operand
                continue  
        elif opcode == 4: 
            B ^= C
        elif opcode == 5: 
            output.append(combo(operand) % 8)
        elif opcode == 6:
            deno = 2 ** combo(operand)
            B = A // deno
        elif opcode == 7:
            deno = 2 ** combo(operand)
            C = A // deno
        
        p += 2 
    return output

print(','.join(map(str, (simulate(A, B, C)))))

def solve(c): # sourced from fogleman
    for i in range(8):
        nc = (c << 3) + i
        l = simulate(nc)
        if l == program:
            return nc
        if l == program[-len(l):] and (r := solve(nc)):
            return r
print(solve(0))
