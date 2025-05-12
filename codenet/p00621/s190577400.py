class Cat:
    def __init__(self, input):
        self.id = int(input[1])
        self.size = int(input[2])

    def sleep(self, index):
        self.index = index

    def last(self):
        return self.index + self.size

def lastindex(list, val):
    result = len(list) - 1
    for n in range(len(list)):
        if list[n] == val:
            result = n
    return result

def indexSleepable(wall, size):
    index = 0
    while index < len(wall):
        target = wall[index:index+size]
        if target == [False] * size:
            return index
        else:
            next_index = lastindex(target, True)
            index += next_index + 1
    else:
        return -1

while True:
    W, Q = [int(n) for n in input().split() ]

    if W == Q == 0:
        break

    lines = [input().strip().split() for n in range(Q) ]

    wall = [False] * W

    Catdict = {}

    for l in lines:
        if l[0] == "s":
            cat = Cat(l)
            index = indexSleepable(wall, cat.size)
            if index != -1:
                cat.sleep(index)
                print(index)
                wall[cat.index:cat.last()] = [True] * cat.size
                Catdict[cat.id] = cat
            else:
                print("impossible")
        elif l[0] == "w":
            cat = Catdict[int(l[1])]
            wall[cat.index:cat.last()] = [False] * cat.size

    print("END")