inputs = [line.rstrip('\n') for line in open("inputs/01.txt")]

def one():
    numbers = []
    for i in inputs:
        
        num = ''.join(char for char in i if char.isdigit())
        if len(num) > 2:
            newnum = num[0] + num[-1]
        elif len(num) == 1:
            newnum = num + num
        else:
            newnum = num

        numbers.append(int(newnum))
    print(sum(numbers))
    
def two():
    nums =[]
    words = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tonum = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i in inputs:
        d = {}
        for w in words:
            index = 0
            while w in i[index:]:
                if w in tonum:
                    new = tonum[w]
                else:
                    new = w
                newindex = i[index:].find(w)
                d[newindex + index] = new
                index += newindex + 1
        mi = min(d)
        ma = max(d)
        nums.append(int(d[mi] + d[ma]))
    print(sum(nums))

one()
two()

