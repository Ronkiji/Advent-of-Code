import itertools

with open("inputs/day19.txt") as fp:
  rules, messages = fp.read().split('\n\n')
  rules = rules.splitlines()
  messages = messages.splitlines()

r = {}

for rule in rules:
  key, val = rule.split(': ')
  if val[0] == '"':
    r[int(key)] = val[1 : -1]
  else:
    val = val.split(' | ')
    temp = []
    for v in val:
      temp.append([int(x) for x in v.split(' ')])
    r[int(key)] = temp

def find(index):
  global r
  answers = []
  for set in r[index]:
    possibilities = []
    for s in set:
      if r[s] == 'a' or r[s] == 'b':
        possibilities.append([r[s]])
      else:
        possibilities.append(find(s))
    for list in itertools.product(*possibilities):
      answer = ''
      for x in range(len(list)):
        answer += list[x]
      answers.append(answer)
  return answers

def match(ms, arr):
  count = 0
  for m in ms:
    if m in arr:
      count += 1
  return count

print('count is : ' + str(match(messages, find(0))))