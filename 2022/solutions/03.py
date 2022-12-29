inputs = [line.rstrip('\n') for line in open("inputs/03.txt")]

def one():
    intersects = []
    for string in inputs:
        half = len(string) // 2
        one = string[:half]
        two = string[half:]
        intersects.append([element for element in one if element in two])
        
    counter = 0
    for i in intersects:
        char = i[0]
        if ord(char) < 96:
            counter += ord(char) - 38
        else: 
            counter += (ord(char) - 96)
        

    print(counter)
    
def two():
    intersects = []
    for x in range(len(inputs) // 3):
        index = 3 * x
        one = set(inputs[index])
        two = set(inputs[index + 1])
        three = set(inputs[index + 2])
        
        set1 = one.intersection(two)
        result = set1.intersection(three)
        
        intersects.append(result)
        
    counter = 0
    for i in intersects:
        char1 = list(i)
        char = char1[0]
        if ord(char) < 96:
            counter += ord(char) - 38
        else: 
            counter += (ord(char) - 96)

    print(counter)

one()
two()
    