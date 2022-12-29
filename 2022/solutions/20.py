inputs = [int(line.rstrip('\n')) for line in open("inputs/20.txt")]

def part(multiplier, mixes):
    
    enum = [(i, x * multiplier) for (i, x) in enumerate(inputs)]
    length = len(enum)
    
    for mix in range(mixes):
        
        for k in range(length):

            for i in range(length):
                if enum[i][0] == k:
                    index = i
                    
            node = enum[index]
            val = node[1]
            
            enum = enum[:index] + enum[(index+1):]
            offset = (index + val) % (length - 1)
            enum = enum[:offset] + [node] + enum[offset:]

    i = [j for j in range(length) if enum[j][1] == 0][0]
    print(enum[(i + 1000) % length][1] + enum[(i + 2000) % length][1] + enum[(i + 3000) % length][1])

part(1, 1) # one
part(811589153, 10) # two
