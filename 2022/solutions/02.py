parse = [(line.rstrip('\n')) for line in open("inputs/02.txt")]
inputs = [[key, val] for key, val in (line.split(" ") for line in parse)]


def one():
    score = 0
    for s in inputs:
        y = s[0]
        x = s[1]
        
        if x == 'X':
            if y == 'A':
                score += 1 + 3
            elif y == 'B':
                score += 1 + 0
            elif y == 'C':
                score += 1 + 6
                
        elif x == 'Y':
            if y == 'A':
                score += 2 + 6
            elif y == 'B':
                score += 2 + 3
            elif y == 'C':
                score += 2 + 0
        
        elif x == 'Z':
            if y == 'A':
                score += 3 + 0
            elif y == 'B':
                score += 3 + 6
            elif y == 'C':
                score += 3 + 3
                
    print(score)

def two():
    score = 0
    for s in inputs:
        y = s[0]
        x = s[1]
        
        if x == 'X':
            if y == 'A':
                score += 3 + 0
            elif y == 'B':
                score += 1 + 0
            elif y == 'C':
                score += 2 + 0
                
        elif x == 'Y':
            if y == 'A':
                score += 1 + 3
            elif y == 'B':
                score += 2 + 3
            elif y == 'C':
                score += 3 + 3
        
        elif x == 'Z':
            if y == 'A':
                score += 2 + 6
            elif y == 'B':
                score += 3 + 6
            elif y == 'C':
                score += 1 + 6
            
    print(score)
    
one()
two()