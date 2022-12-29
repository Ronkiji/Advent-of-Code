def part2():
  inputs = []
  fullLine = ''
  for line in open("inputs/day04.txt"):
    line = line.rstrip('\n')
    if line != '':
      fullLine += line + ' '
    elif line == '':
      fullLine = fullLine.rstrip('\n')
      inputs.append(fullLine)
      fullLine = ''
  if fullLine != '': inputs.append(fullLine)

  elements = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

  count = 0
  results = []

  valids = []

  for line in inputs:
    for substrings in elements:
      results.append(substrings in line)
    if all(results):
      valids.append(line)
      count += 1
    results = []

  keyval = []

  full = []

  for line in valids:
    for field in line.split():
      key, value = field.split(':')
      keyval.append([key, value])
    full.append(keyval)
    keyval = []

  num = 0
  total = 0


  for line in full:
    for x in line:
      
      # for years
      if x[0] == 'byr':
        if 1920 <= int(x[1]) <= 2002:
          num += 1
      elif x[0] == 'iyr':
        if 2010 <= int(x[1]) <= 2020:
          num += 1
      elif x[0] == 'eyr':
        if 2020 <= int(x[1]) <= 2030:
          num += 1
      
      # for height
      elif x[0] == 'hgt':
        if x[1].find('cm') != -1:
          hgtcm = int(x[1][0 : -2])
          if 150 <= hgtcm <= 193:
            num += 1
        elif x[1].find('in') != -1:
          hgtin = int(x[1][0 : -2])
          if 59 <= hgtin <= 76:
            num += 1

      # for colors
      elif x[0] == 'hcl':
        hcl = x[1][1:]
        if len(hcl) == 6:
          charvalid = 0
          for char in hcl:
            if char.isnumeric() and 0 <= int(char) <= 9:
              charvalid += 1
            elif 'a' <= char <= 'f':
              charvalid += 1
          if charvalid == 6:
            num += 1    
        
      elif x[0] == 'ecl':
        if x[1] == 'amb' or x[1] == 'blu' or x[1] == 'brn' or x[1] == 'gry' or x[1] == 'grn' or x[1] == 'hzl' or x[1] == 'oth':
          num += 1

      # for ID
      elif x[0] == 'pid':
        if x[1].isnumeric() and len(x[1]) == 9:
          num += 1
    
    if num == 7:
      total += 1
    num = 0

  return total

print(part2())