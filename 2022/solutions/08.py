inputs = [line.rstrip('\n') for line in open("inputs/08.txt")]

xmax = len(inputs[0])
ymax = len(inputs)

def one():
    
    trees = 0
    for x in range(xmax):
        for y in range(ymax):
            visible = [True, True, True, True]
            height = int((inputs[y][x]))
            for newx in range(x-1, -1, -1):
                if int((inputs[y][newx])) >= height:
                    visible[0] = False
            for newx in range(x + 1, xmax):
                if int((inputs[y][newx])) >= height:
                    visible[1] = False
            for newy in range(y-1, -1, -1):
                if int((inputs[newy][x])) >= height:
                    visible[2] = False
            for newy in range(y + 1, ymax):
                if int((inputs[newy][x])) >= height:
                    visible[3] = False
            if any(visible):
                trees += 1

    print(trees)


def two():

    points = []
    for x in range(xmax):
        for y in range(ymax):
            height = int((inputs[y][x]))
            l = 0
            for newx in range(x-1, -1, -1):
                l += 1
                if int((inputs[y][newx])) >= height:
                    break
            r = 0
            for newx in range(x + 1, xmax):
                r += 1
                if int((inputs[y][newx])) >= height:
                    break
            b = 0
            for newy in range(y-1, -1, -1):
                b += 1
                if int((inputs[newy][x])) >= height:
                    break
            t = 0
            for newy in range(y + 1, ymax):
                t += 1
                if int((inputs[newy][x])) >= height:
                    break
            points.append(l * r * b * t)

    print(max(points))

one()
two()