# empty lines cannot be cast as ints or anyhting else, hence from the inputs, cast int

# stores list of ints in 'inputs'
inputs = [int(line.rstrip('\n')) for line in open("inputs/25.txt")]

# 001000010101
# 010010111110
# 001010110111


# stores list of strings in 'inputs'
inputs = [line.rstrip('\n') for line in open("inputs/25.txt")]

# 100
# 200
# 300


# stores list of tuples (key, val) in 'inputs'
parse = [(line.rstrip('\n')) for line in open("inputs/25.txt")]
inputs = [[key, int(val)] for key, val in (line.split(" ") for line in parse)]

# forward 1
# forward 2
# down 5

# stores list of single variables in 'inputs'
parse = [(line.rstrip('\n')) for line in open("25.txt")]
inputs = [int(num) for num in input[0].split(",")]

#1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65

# list declaration
a_list = []
a_list.append(0)

# dict declaration
a_dict = {}
a_dict["1"] = "one" 
keys = a_dict.keys
values = a_dict.values


# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    # print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))

# if(dict[key] != None):

# new_set = set(filter(lambda x: x[0] != delete_value, s))

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "%": lambda x, y: x % y,
    "**": lambda x, y: x ** y
}

op = lambda x, y, o: eval(x + o + y)


