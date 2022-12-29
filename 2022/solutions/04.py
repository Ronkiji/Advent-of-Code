parse = [(line.rstrip('\n')) for line in open("inputs/04.txt")]
inputs = [[key, val] for key, val in (line.split(",") for line in parse)]

def one():
    counter = 0
    for duple in inputs:
        one = duple[0].split("-")
        two = duple[1].split("-")
                
        if int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[1]):
            counter += 1
        elif int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1]):
            counter += 1

    print(counter)


def two():
    counter = 0
    for duple in inputs:
        one = duple[0].split("-")
        two = duple[1].split("-")

        
        if int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[0]):
            counter += 1
        elif int(one[0]) <= int(two[1]) and int(one[1]) >= int(two[1]):
            counter += 1
        elif int(two[0]) <= int(one[0]) and int(two[1]) >= int(one[0]):
            counter += 1
        elif int(two[0]) <= int(one[1]) and int(two[1]) >= int(one[1]):
            counter += 1
            
    print(counter)


one()
two()