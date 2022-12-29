inputs = open("inputs/11.txt").read().rstrip().split("\n\n")

monkeys = {}

for i, monkey in enumerate(inputs):
    monkey = monkey.split("\n")
    monkeys[i] = {}
    monkeys[i]["items"] = [int(i) for i in monkey[1].split(": ")[1].split(",")]
    monkeys[i]["op"] = monkey[2].split("= old ")[1]
    monkeys[i]["div"] = int(monkey[3].split("by ")[1])
    monkeys[i][True] = int(monkey[4].split("monkey ")[1])
    monkeys[i][False] = int(monkey[5].split("monkey ")[1])

mcount = len(monkeys)
inspect = [0] * mcount

operations = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}

mod = 1
for n in monkeys:
    mod *= monkeys[n]["div"]

def find(rounds, part):
    
    for rounds in range(rounds):
        for m in range(mcount):
            monkey = monkeys[m]
            for item in monkey["items"][:]:
                op, num = monkey["op"].split(" ")
                num = item if num == "old" else int(num)
                newlvl = operations[op](item, num)
                newlvl = newlvl // 3 if part == 1 else newlvl % mod
                x = monkey[newlvl % monkey["div"] == 0]
                monkeys[x]["items"].append(newlvl)
                monkey["items"].pop(0)
                inspect[m] += 1
    inspect.sort(reverse=True)
    print(inspect[0] * inspect[1])

# part 1
find(20, 1)
# part 2
find(10000, 2)
            