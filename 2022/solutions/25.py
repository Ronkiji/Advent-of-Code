inputs = [line.rstrip('\n') for line in open("inputs/25.txt")]
counter = 0

for line in inputs:
    power = 0
    nums = reversed(list(line))
    for n in nums:
        if n == '=':
            counter -= 2 * pow(5, power)
        elif n == '-':
            counter -= pow(5, power)
        else:
            counter += int(n) * pow(5, power)
        power += 1
print(counter)

snafu = ""

while counter:
    remainder = counter % 5
    if remainder <= 2:
        snafu = str(remainder) + snafu
        counter = counter // 5
    else:
        snafu = '=' + snafu if remainder == 3 else '-' + snafu
        counter = counter // 5 + 1
print(snafu)